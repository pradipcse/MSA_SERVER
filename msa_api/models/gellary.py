# models.py

from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    date = models.DateField()

    def __str__(self):
        return self.title
