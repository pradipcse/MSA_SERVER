from django.db import models

class Advisor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='advisor_images/')
    work_place = models.CharField(max_length=255)
    biography = models.TextField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(unique=True)
    profile_link = models.URLField()
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name
