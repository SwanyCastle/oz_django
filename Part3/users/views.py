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