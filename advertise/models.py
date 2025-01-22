from django.db import models

# Create your models here.
class AdvertiseModel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image=models.ImageField(upload_to="advertise/images")