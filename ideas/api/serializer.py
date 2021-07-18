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
    goods_count = serializers.SerializerMethodField()
    is_good = serializers.SerializerMethodField()
    
    class Meta:
        model = Idea
        fields = ("id", "user_id", "title", "content", "goods_count", "is_good")
    
    def get_goods_count(self, obj):
        return obj.goods.count()

    def get_is_good(self, obj):
        user = self.context['request'].user

        if user.is_authenticated:
            return Good.objects.filter(user_id=user, idea_id=obj).exists()
        else:
            return False

class IdeaSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Idea
        fields = ("user_id", "title", "content", "comments")
        # fields = "__all__"

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Good
        fields = "__all__"