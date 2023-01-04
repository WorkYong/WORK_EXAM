from django.db   import models

from users.models import User
from core.models  import TimeStampModel

class AccountBook(TimeStampModel): 
    book_name  = models.CharField(max_length = 100)
    is_deleted = models.BooleanField()
    user       = models.ForeignKey(User, on_delete = models.CASCADE)
    deleted_at = models.DateTimeField(null = True, default = None)
    
    class Meta:
        db_table = 'accountbooks'
