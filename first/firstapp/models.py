from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=264,unique=True)
    last_name=models.CharField(max_length=264,unique=True)
    email=models.URLField(unique=True)

    def __str__(self):
        return self.name

# Create your models here.
