from msilib.schema import Class
from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    CHOICES = (

        (Role.USER, 'user'),
        (Role.MODERATOR, 'moderator'),
        (Role.ADMIN, 'admin'),

    )
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(
        verbose_name='email адрес',
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=15, choices=CHOICES, default='user')
    bio = models.TextField(blank=True, null=True)
    USERNAME_FIELD = 'username'
