from django.db import models
from rest_framework import serializers
from ideas.models import Idea

class IdeaSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)
    class Meta:
        model = Idea
        # fields = "__all__"
    # def create(self, validated_data):
    
    def save(self):
        user_id = self.context['request'].user
        content = self.validated_data['content']
    
    