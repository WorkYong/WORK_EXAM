from django.db   import models

from core.models import TimeStampModel

'''user models'''

'''email값의 unique = true를 주어 중복되는 값은 DB에 들어가지 못하도록 처리하였습니다. 
    is_active 상태 값 Column을 만들어 soft_delte를 할 수 있도록 설계하였습니다.
    기본값은 True로 선언하여 따로 지정하지 않으면 1값으로 저장됩니다.'
    is_active 가 false(=0)로 바뀌게되면 탈퇴회원으로 식별합니다.'''

class User(TimeStampModel): 
    name         = models.CharField(max_length = 50)
    password     = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 100)
    email        = models.CharField(max_length = 200, unique=True)
    is_active    = models.BooleanField(default = True)

    class Meta:
        db_table = 'users'