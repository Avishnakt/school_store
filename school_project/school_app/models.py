from django.db import models


# Create your models here.

class Store(models.Model):
    username = models.CharField(max_length=250, unique=True)
    dob = models.DateField()
    age = models.IntegerField()
    number = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.username
