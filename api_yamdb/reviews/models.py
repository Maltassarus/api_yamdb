from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Ссылка'
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(
        Category,
        related_name='categories',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Ссылка'
    )
    title = models.ForeignKey(
        Title,
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Reviews(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='titles',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
    )
    score = models.IntegerField()
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        Reviews,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )
