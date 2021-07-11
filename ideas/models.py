from os import name, nice
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

class Idea(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=CASCADE)
    content = models.CharField(max_length=255)

class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    idea_id = models.ForeignKey(Idea, on_delete=CASCADE)
    comment = models.CharField(max_length=100)

class Good(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    idea_id = models.ForeignKey(Idea, on_delete=CASCADE)



