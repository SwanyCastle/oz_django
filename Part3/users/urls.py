from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.Users.as_view()),
    path('myinfo', views.MyInfo.as_view()),
    path('getToken',obtain_auth_token),
]