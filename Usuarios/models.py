from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    email = models.EmailField(
        unique=True, 
        blank=False,
        verbose_name="Correo Electrónico"
    )
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"