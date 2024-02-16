from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Feed
from users.models import User
from .serializers import FeedSerializer

# api/v1/feeds [POST]

class Feeds(APIView):
    # 전체 게시글 조회
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        # data = request.data
        # user = User.objects.get(username=data['user']['username'])
        # feed = Feed(title=data['title'], content=data['content'], user=user)
        # feed.save()
        # serializer = FeedSerializer(feed)
        # return Response(serializer.data)
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            # print(serializer.data)
            return Response(serializer.data)
        else:
            print(serializer.data)
            return Response(serializer.errors)

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)
    

# {
#     "user": {
#         "username": "seunghwan",
#         "email": "seunghwan@gmail.com",
#         "is_superuser": true
#     },
#     "created_at": "2024-02-16T12:11:29.286792+09:00",
#     "updated_at": "2024-02-16T12:11:29.286824+09:00",
#     "title": "세번째 피드",
#     "content": "세번째 피드 입니다 -.-"
# }