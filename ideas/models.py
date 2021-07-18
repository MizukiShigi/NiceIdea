from os import name, nice
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Idea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, blank=True, null=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=CASCADE, blank=True, null=True)
    idea = models.ForeignKey(Idea, on_delete=CASCADE, related_name='comments', blank=True, null=True)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Good(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, blank=True, null=True)
    idea = models.ForeignKey(Idea, on_delete=CASCADE, related_name='goods', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



