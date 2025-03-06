from django.db import models
from django.core.exceptions import ValidationError
import mimetypes

class UpdateAndNotice(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='updates_and_notices/', null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    # Custom file validation method directly in the model
    def clean(self):
        super().clean()

        # Validate file extension
        if self.file:
            allowed_extensions = ['pdf', 'txt', 'jpg', 'jpeg', 'png']
            file_extension = self.file.name.split('.')[-1].lower()
            
            if file_extension not in allowed_extensions:
                raise ValidationError(f"File type {file_extension} is not allowed. Only PDF, TXT, JPG, JPEG, PNG files are allowed.")
            
            # Optional: Check mime type for more security (basic validation)
            mime_type, _ = mimetypes.guess_type(self.file.name)
            allowed_mimes = ['application/pdf', 'text/plain', 'image/jpeg', 'image/png']
            
            if mime_type not in allowed_mimes:
                raise ValidationError(f"Invalid mime type: {mime_type}. Only PDF, TXT, JPG, JPEG, PNG are allowed.")
