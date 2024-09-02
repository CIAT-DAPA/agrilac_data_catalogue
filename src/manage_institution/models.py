from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Institution(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_institutions')
    is_certified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=False)
    phone = models.CharField(
        max_length=15,
        blank=False,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.")]
    )

    def clean(self):
        super().clean()
        if '@example.com' in self.email:
            raise ValidationError('El uso de correos electrónicos de "example.com" no está permitido.')

    def __str__(self):
        return self.name