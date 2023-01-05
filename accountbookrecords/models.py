from django.db import models

from users.models        import User
from accountbooks.models import AccountBook
from core.models         import TimeStampModel

class AccountBookRecord(TimeStampModel): 
    title        = models.CharField(max_length = 100)
    date         = models.CharField(max_length = 150)
    memo         = models.CharField(max_length = 200)
    description  = models.CharField(max_length = 300)
    amount       = models.CharField(max_length = 200)
    balance      = models.CharField(max_length = 200)
    serial_no    = models.CharField(max_length = 200)
    is_deleted   = models.BooleanField(default = True)
    account_book = models.ForeignKey(AccountBook, on_delete = models.CASCADE)
    user         = models.ForeignKey(User, on_delete = models.CASCADE)
    deleted_at   = models.DateTimeField(null = True, default = None)

    
    class Meta:
        db_table = 'accountbookrecords'

