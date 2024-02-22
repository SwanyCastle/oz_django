from rest_framework.serializers import ModelSerializer

from users.serializers import FeedUserSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    user = FeedUserSerializer()
    class Meta:
        model = Review
        fields = "__all__"