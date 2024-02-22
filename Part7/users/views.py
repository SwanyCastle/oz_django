from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from django.contrib.auth.password_validation import validate_password

# 어떤 유저인지를 식별하기 위한 느낌이라고 볼 수 있음 - 인증
from rest_framework.authentication import TokenAuthentication
# 인증된 유저들만이 볼 수 있도록 권한을 부여하는 느낌이라고 볼 수 있음 - 권한
from rest_framework.permissions import IsAuthenticated

from .serializers import MyInfoUserSerializer

# api/v1/users [POST] -> 유저 생성 API
class Users(APIView):
    def post(self, request):
        # password -> 검증 / 해쉬화 저장
        # the other -> 비밀번호 외 다른 데이터들

        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # set_password() 로 비밀번호 해쉬화
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)
        
# api/v1/users/myinfo [GET, PUT]
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)

        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True) 
        # partial=True -> 원래는 User 모델에 필요한 데이터를 전체적으로 넘겨 줘야하는데 
        #                 이 옵션을 사용하면 부분적으로 넘겨주어도 됨

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# BasicAuth(Session로그인)
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
# api/v1/users/login
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError("request not usernae or password")
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
# api/v1/users/logout
class Logout(APIView):
    # 로그인한 유저인지 체크 하기 위해
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print("header : ", request.headers)
        logout(request)

        return Response(status=status.HTTP_200_OK)
    

from django.conf import settings
import jwt
# api/v1/users/login/jwt
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError("request not username / password")
        
        user = authenticate(request, username=username, password=password)

        if user:
            payload = {"id": user.id, "username": user.username}
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256"
            )
            return Response({"token": token})
        
# api/v1/users/login/jwt/info
from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    # simplejwt 로 생성된 access token을 이용해서 접근하려면 
    # 아래에 우리가 수동으록 만들어준 Django jwt 토큰을 사용하면 에러가 뜸
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "username": user.username
        })
    