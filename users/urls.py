from django.urls.conf import path
from .views import AuthRegister, AuthInfoGetView

urlpatterns = [
    path("register/", AuthRegister.as_view()),
    path("mypage/", AuthInfoGetView.as_view()),
]