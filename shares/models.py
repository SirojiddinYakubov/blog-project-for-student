from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='articles')
    claps = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('clap', 'Clap'),
        ('like', 'Like'),
    ]
    type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    link = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
