from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.age})'
