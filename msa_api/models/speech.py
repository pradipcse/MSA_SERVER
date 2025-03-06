from django.db import models

class Speech(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_images/')
    designation = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
