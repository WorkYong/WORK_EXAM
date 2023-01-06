from django.db import models

'''
자주사용하는 Timestamp(생성시기, 수정시기)를 다른 모델에서 Import하여 
사용하기 편하게 만들었습니다.
'''

class TimeStampModel(models.Model):
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
