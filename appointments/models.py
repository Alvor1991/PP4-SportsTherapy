from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model extending the built-in AbstractUser
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
