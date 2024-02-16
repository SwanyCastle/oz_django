from django.db import models

class CommonModel(models.Model):
    # auto_now_add -> 데이터가 생성 될 때, 현재 시간을 자동적으로 추가 - 이후 데이터가 업데이트 되어도 수정되지 않음
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now -> 데이터가 업데이트 될 때, 현재 시간을 자동적으로 업데이트
    updated_at = models.DateTimeField(auto_now=True)

    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용
    class Meta:
        abstract = True # DB 테이블에 추가하는 것을 원하지 않는다.