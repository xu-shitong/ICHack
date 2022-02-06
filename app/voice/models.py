from django.db import models

# Create your models here.
class Song(models.Model):
    """
    Audio file
    """
    title = models.CharField(max_length=100)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)

