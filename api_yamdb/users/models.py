from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user', ('Пользователь')
        MODERATOR = 'moderator', ('Модератор')
        ADMIN = 'admin', ('Администратор')

    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.USER,
    )
    bio = models.TextField(blank=True, null=True)
