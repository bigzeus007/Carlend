from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('employee', 'Employé'),
        ('validator', 'Validateur'),
        ('pending', 'En attente')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='pending')

    def is_admin(self):
        return self.role == 'admin'
    
    def is_employee(self):
        return self.role == 'employee'
    
    def is_validator(self):
        return self.role == 'validator'
