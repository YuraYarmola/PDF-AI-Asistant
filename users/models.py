from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
