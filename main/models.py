from django.db import models

# Create your models here.

class Userss(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username