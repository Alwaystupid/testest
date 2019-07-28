from django.db import models

# Create your models here.

class Owner(models.Model):
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField()


class Pet(models.Model):
    TYPE = (
        ('C', 'Cat'),
        ('D', 'Dog')
    )
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE)
