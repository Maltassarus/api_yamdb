from django.db import models
from users.models import User


class Reviews(models.Model):
    title = models.ForeignKey()
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
