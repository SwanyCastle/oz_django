from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
	TokenVerifyView
)

from . import views

urlpatterns = [
    path('', views.Users.as_view()),
    path('myinfo', views.MyInfo.as_view()),

    # Authentication
    path('getToken',obtain_auth_token), # DRF Token
    path('login',views.Login.as_view()), #Django Session Login
    path('logout',views.Logout.as_view()), #Django Session Logout

    # JWT Authentication
    path('login/jwt', views.JWTLogin.as_view()), # JWT Token
    path('login/jwt/info', views.UserDetailView.as_view()), # JWT Token Check

    # Simple Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# login 정보
# {
#     "username": "seunghwan",
#     "password": "pw123"
# }

# login 시 발생된 토큰
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJzZXVuZ2h3YW4ifQ.hN5pMS04KBNoQ07oE3_U3wc2vbtyc8aEo7auuDNr5F0