from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import UserManager as manger
from django.db import models

# class UserManager(manger):
#     def create_superuser(
#         self,
#         username,
#         email=None,
#         password=None,
#         **extra_fields
#     ):
#         super().create_superuser(
#             username,
#             email,
#             password,
#             **extra_fields
#         )
#         extra_fields.setdefault('role', 'test')


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
    bio = models.TextField(blank=True)

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email',
            )
        ]
