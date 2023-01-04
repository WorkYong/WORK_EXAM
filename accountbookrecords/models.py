from django.db import models

from accountbooks.models import AccountBook
from core.models         import TimeStampModel

class AccountBookRecord(TimeStampModel): 
    title        = models.CharField(max_length=100)
    date         = models.CharField(max_length=150)
    memo         = models.CharField(max_length=200)
    description  = models.CharField(max_length=300)
    amount       = models.DecimalField(decimal_places=3, max_digits=15)
    balance      = models.DecimalField(decimal_places=3, max_digits=15)
    is_deleted   = models.BooleanField()
    account_book = models.ForeignKey(AccountBook, on_delete = models.CASCADE)
    deleted_at   = models.DateTimeField(null = True, default = None)

    
    class Meta:
        db_table = 'accountbookrecords'

