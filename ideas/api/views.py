from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from ideas.models import Idea, Tag, Good, Comment
from ideas.api.serializer import IdeaListSerializer, IdeaSerializer, CommentSerializer, GoodSerializer
from rest_framework.permissions import IsAuthenticated

class IdeaListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        ideas = Idea.objects.prefetch_related('goods').all().order_by("-created_at")
        serializer = IdeaListSerializer(ideas, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = IdeaListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user.pk)
        return Response(serializer.data)

class IdeaDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):
        idea = Idea.objects.prefetch_related('comments').get(pk=pk)
        serializer = IdeaSerializer(idea)
        return Response(serializer.data)

class CommentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):
        comments = Comment.objects.filter(idea_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user.pk)
        serializer.save(idea_id=pk)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def like(request, pk):
    like = Good.objects.create(user_id=request.user.pk, idea_id=pk)
    like.save()
    return Response({'data': 'Like successfully'})

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def unlike(request, pk):
    if not Good.objects.filter(user_id=request.user.pk, idea_id=pk).exists():
        return Response({'errors': {"You aren't like that post"}}, status=status.HTTP_400_BAD_REQUEST)

    Good.objects.get(user_id=request.user.pk, idea_id=pk).delete()

    return Response({'data': 'Unlike successfully'})
    