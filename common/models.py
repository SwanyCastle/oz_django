from django.db import models

# Create your models here.

class CommonModel(models.Model):
    # auto_now_add = 현재 데이터 생성 시간을 기준으로 생성 -> 이후 데이터가 업데이트 되어도 수정되지 않음
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now = 생성되는 시간 기준으로 일단 생성 -> 이후 데이터가 업데이트 되면 시간도 같이 업데이트됨
    updated_at = models.DateTimeField(auto_now=True)

    # 모든 테이블에 위와 같은 컬럼이 추가가 되어버리면 테이블들이 복잡해 질 수 있기 때문에
    class Meta:
        abstract = True # 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지 않도록 설정
                        # 추상 기반 클래스임을 나타냄 -> 데이터베이스에 직접적으로 맵핑 되지 않으며 테이블을 생성하지 않음