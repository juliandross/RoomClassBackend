from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    rol = models.CharField(max_length=10, default='DOCENTE')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"