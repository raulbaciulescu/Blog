from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=1000000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.text[:200]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # when i delete an user, all posts are deleted
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
