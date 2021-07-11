from django.urls import path
from ideas.api import views

urlpatterns = [
    path("ideas/", views.IdeaListView.as_view(), name="list"),
    path("ideas/<int:pk>/", views.IdeaDetailView.as_view(), name="detail"),
]