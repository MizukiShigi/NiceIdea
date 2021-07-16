from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ideas.models import Idea, Tag, Good, Comment
from ideas.api.serializer import IdeaSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

class IdeaListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        ideas = Idea.objects.all().order_by("-created_at")
        print(ideas)
        serializer = IdeaSerializer(ideas, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = IdeaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user.pk)
        return Response(serializer.data)
    


class IdeaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsAuthenticated,)

class CommentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):
        comments = Comment.objects.filter(idea_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user.pk, idea_id=pk)
        return Response(serializer.data)