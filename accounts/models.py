from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name=User
    )
    phone_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='Phone Number')
    address = models.TextField(null=True, blank=True, verbose_name='Address')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'