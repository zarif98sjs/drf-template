from django.db import models
from django.contrib.auth.models import AbstractUser

## extend the User model this way
class User(AbstractUser):
    about = models.TextField(blank=True)