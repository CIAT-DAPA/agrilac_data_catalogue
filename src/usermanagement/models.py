from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMIN = 'Admin'
    VISITOR = 'Visitor'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (VISITOR, 'Visitor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=VISITOR)

    def __str__(self):
        return self.username