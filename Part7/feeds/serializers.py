from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

# (1) 전체 데이터를 보여주는 Serializer
class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    # read_only=True 로 해야됨 / Feed 를 POST 로 새로 생성 할 때 user 나 review 값이 변하면 안되기 때문
    # 이거 안하면 POST 로 값 추가 할때 is_valid() 에서 결러서 어차피 안들어가짐 ㅡㅡ
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1

# (2) 일부 데이터를 보여주는 Serializer
class FeedListSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "user", "title", "content")