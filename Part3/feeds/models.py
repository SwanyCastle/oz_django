from django.db import models
from common.models import CommonModel

# 제목(title), 내용(content), 작성자(User)

# Feed 와 User 와의 관계
# User -> Feed, Feed, Feed (O)
# Feed -> User, User, User (X)

class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
