from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Class(models.Model):
    teacher = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    classcode = models.TextField()
    classname = models.TextField()

class Questions(models.Model):
    question = models.TextField()
    type = models.TextField()

class Results(models.Model):
    code = models.TextField()
    name = models.TextField()
    VERB = models.IntegerField(default=0)
    LOG = models.IntegerField(default=0)
    MUS = models.IntegerField(default=0)
    VIS = models.IntegerField(default=0)
    KIN = models.IntegerField(default=0)
    INTER = models.IntegerField(default=0)
    INTRA = models.IntegerField(default=0)
    NAT = models.IntegerField(default=0)