from django.db import models

# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
