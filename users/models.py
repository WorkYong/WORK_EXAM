from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel): 
    name         = models.CharField(max_length = 50)
    password     = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 100)
    email        = models.CharField(max_length = 200, unique=True)
    is_active    = models.BooleanField(default = True)

    class Meta:
        db_table = 'users'