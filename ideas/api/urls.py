from django.urls import path
from ideas.api import views

urlpatterns = [
    path("ideas/", views.IdeaListView.as_view(), name="ideas"),
    path("ideas/<int:pk>/", views.IdeaDetailView.as_view(), name="idea"),
    path("ranking/", views.RankingView.as_view(), name="ranking"),
    path("myideas/", views.MyIdeaView.as_view(), name="myidea"),
    path("comments/<int:pk>/", views.CommentView.as_view(), name="comments"),
    path("idea/<int:pk>/like/", views.like, name="like"),
    path("idea/<int:pk>/unlike/", views.unlike, name="unlike"),
]