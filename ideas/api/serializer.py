from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework import serializers
from ideas.models import Idea, Comment
from django.conf import settings

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    # idea = models.ForeignKey(Idea, on_delete=CASCADE)
    # comment = models.CharField(max_length=100)
    # def create(self, validated_data):
    #     return Comment(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.idea = validated_data.get('idea', instance.idea)
    #     instance.comment = validated_data.get('comment', instance.comment)
    #     return instance
    class Meta:
        model = Comment
        fields = "__all__"
    