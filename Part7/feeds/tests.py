from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

from .models import Feed
from users.models import User

class FeedAPITestCase(APITestCase):
    # 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
        # 테스트용 유저와 두개의 게시글을 생성
        self.user = User.objects.create_user(username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)

        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.feed1 = Feed.objects.create(user=self.user, title='title1')
        self.feed2 = Feed.objects.create(user=self.user, title='title2')

    def test_get_all_feeds(self):
        url = reverse("all_feeds")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_user_feeds(self):
        url = reverse("user_feeds", kwargs={'feed_id':1})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data['title'], self.feed1.title)

    def test_create_feed(self):
        self.client.login(username='testuser', password='password')
        
        url = reverse("all_feeds")
        data = {'content': 'New Feed', 'title': 'New Title'}
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Feed.objects.count(), 3
        )  # 전체 게시글의 갯수는 3개여야 합니다.
        self.assertEqual(Feed.objects.latest("id").content, "New Feed")

