from django.db import models

# Create your models here.
class Music(models.Model):
    """
    Audio file
    """
    title = models.CharField(max_length=100)


