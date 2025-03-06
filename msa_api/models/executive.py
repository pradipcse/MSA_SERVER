from django.db import models
from rest_framework import serializers

class ExecutiveCommittee(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='executive_images/')
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    session = models.CharField(max_length=50)
    biography = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    fb_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
