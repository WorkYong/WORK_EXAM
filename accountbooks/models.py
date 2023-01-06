from django.db   import models

from users.models import User
from core.models  import TimeStampModel

'''
가계부 모델
이 곳은 상세내역이 아닌 가게부 1권이라고 생각하시면 좀 더 이해가 쉬울거 같습니다.
User 모델과 마찬가지로 상태 값(is_delted)를 주어 soft delete 처리하도록 설계하였습니다.
'''


class AccountBook(TimeStampModel): 
    book_name  = models.CharField(max_length = 100)
    is_deleted = models.BooleanField(default = True)
    user       = models.ForeignKey(User, on_delete = models.CASCADE)
    deleted_at = models.DateTimeField(null = True, default = None)
    
    class Meta:
        db_table = 'accountbooks'