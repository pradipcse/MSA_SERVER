from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    event_details = models.TextField()
    banner = models.ImageField(upload_to='event_banners/', null=True, blank=True)

    def __str__(self):
        return self.title
