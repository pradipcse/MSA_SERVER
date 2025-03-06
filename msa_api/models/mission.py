from django.db import models
class Mission(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]