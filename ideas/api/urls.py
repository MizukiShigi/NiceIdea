from django.urls import path
from ideas.api import views

urlpatterns = [
    path("ideas/", views.IdeaListView.as_view(), name="ideas"),
    path("ideas/<int:pk>/", views.IdeaDetailView.as_view(), name="idea"),
    path("comments/<int:pk>/", views.CommentView.as_view(), name="comments"),
]