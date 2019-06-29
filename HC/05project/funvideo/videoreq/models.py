from django.db import models

# Create your models here.

class videoForm(models.Model):
	videotitle = models.CharField(max_length = 50)
	videodesc = models.TextField()
