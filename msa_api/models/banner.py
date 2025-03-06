from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.image.name