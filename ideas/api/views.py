from rest_framework import generics
from ideas.models import Idea, Tag, Good, Comment
from ideas.api.serializer import IdeaSerializer
from rest_framework.permissions import IsAuthenticated

class IdeaListView(generics.ListCreateAPIView):
    queryset = Idea.objects.all().order_by("created_at")
    serializer_class = IdeaSerializer
    permission_classes = (IsAuthenticated,)

class IdeaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsAuthenticated,)