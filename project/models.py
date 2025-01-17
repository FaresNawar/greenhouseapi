from django.db import models

# Create your models here.

class Status(models.Model):
    image= models.TextField(max_length=200)
    predict_class=models.TextField(max_length=50)
    predict_presntage=models.FloatField(max_length=50)