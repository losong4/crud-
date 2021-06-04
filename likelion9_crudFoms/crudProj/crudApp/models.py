from django.db import models
from django.conf import settings # 프로젝트에서 사용하는 user를 import하기 위해 settings를 가져오기

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published') # null값을 방지하기 위해 default 값을 넣어주는 과정
    writer = models.CharField(null = False, max_length=15, default='닉네임을 입력해주세요')
    body = models.TextField()

# 이름은 바꿀 수 있음, body 대신 content 사용 가능
    def __str__(self):
        return self.title