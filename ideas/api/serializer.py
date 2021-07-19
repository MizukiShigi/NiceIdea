from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from rest_framework import serializers
from ideas.models import Good, Idea, Comment
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"

class IdeaListSerializer(serializers.ModelSerializer):
    comments_count =  serializers.StringRelatedField()
    goods_count = serializers.StringRelatedField()
    is_good = serializers.SerializerMethodField()
    
    class Meta:
        model = Idea
        fields = ("id", "user_id", "title", "content", "comments_count", "goods_count", "is_good")
        read_only_fields = ("comments_count", "goods_count", "is_good")
    
    def get_is_good(self, obj):
        return Good.objects.filter(user_id=self.context['request'].user, idea_id=obj).exists()

class IdeaSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    goods_count = serializers.IntegerField()
    is_good = serializers.SerializerMethodField()
    is_myidea = serializers.BooleanField()
    class Meta:
        model = Idea
        fields = ("id", "user_id", "title", "created_at", "content", "comments", "goods_count", "is_good", "is_myidea")
        read_only_fields = ("comments_count", "goods_count", "is_good", "is_myidea")

    def get_is_good(self, obj):
        return Good.objects.filter(user_id=self.context['request'].user, idea_id=obj).exists()
