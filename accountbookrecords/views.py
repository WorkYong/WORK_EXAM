import json
import uuid

from json.decoder         import JSONDecodeError

from django.http          import JsonResponse
from django.views         import View
from django.utils         import timezone
from django.db.models     import Q

from accountbookrecords.models  import AccountBookRecord
from core.utils           import LoginAccess , shortUrl

class AccountBookRecordView(View):
    @LoginAccess
    def post(self, request):
        try:
            data            = json.loads(request.body)
            title           = data['title']
            date            = data['date']
            memo            = data['memo']
            description     = data['description']
            amount          = data['amount']
            balance         = data['balance']
            account_book_id = data['book_id']
            user_id         = request.user.id
            serial_no       = uuid.uuid4()
            
            AccountBookRecord.objects.create( 
              title           = title,
              date            = date,
              memo            = memo,
              description     = description,
              amount          = amount,
              balance         = balance,
              user_id         = user_id,
              account_book_id = account_book_id,
              serial_no       = serial_no
            )
            return JsonResponse({'message':'SUCCESS', 'RECORD_SERIAL_NO' : serial_no}, status = 201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
    
    @LoginAccess
    def get(self, request):
        account_book_id = request.GET.get('book_id')
        serial_no       = request.GET.get('serial_no')
        is_deleted      = request.GET.get('is_deleted')
        queries         = Q()
        
        if account_book_id :
          queries &= Q(account_book_id = account_book_id)

        if serial_no :  
          queries &= Q(serial_no = serial_no)

        if is_deleted :
          queries &= Q(is_deleted = is_deleted)

        accountbookrecords = AccountBookRecord.objects.filter(queries)
        
        result = [
        {
          'id'         : accountbookrecord.id,
          'title'      : accountbookrecord.title,
          'date'       : accountbookrecord.date,
          'memo'       : accountbookrecord.memo,
          'description': accountbookrecord.description,
          'amount'     : accountbookrecord.amount,
          'balance'    : accountbookrecord.balance,
          'is_deleted' : accountbookrecord.is_deleted,
          'created_at' : accountbookrecord.created_at,
          'updated_at' : accountbookrecord.updated_at,
          
        } for accountbookrecord in accountbookrecords]

        shortUrl(account_book_id, serial_no, is_deleted)
        return JsonResponse({"result":result, "short_url":shortUrl(account_book_id, serial_no, is_deleted)}, status = 200)

    @LoginAccess
    def patch(self, request):
        try: 
            data                 = json.loads(request.body)
            accountbookrecord_id = data['record_id']
            is_deleted           = False

            accountbookrecords   = AccountBookRecord.objects.get(
              id                 = accountbookrecord_id,
              user_id            = request.user.id)

            if is_deleted == False:
                accountbookrecords.is_deleted = False
                accountbookrecords.deleted_at = timezone.now()
                accountbookrecords.save()
                
                return JsonResponse({'message':'DELETE','is_deleted': accountbookrecords.is_deleted, 'deleted_at':accountbookrecords.deleted_at}, status = 200)
            else :
                return JsonResponse({'message':"BAD REQUEST"}, status = 400) 

        except AccountBookRecord.DoesNotExist :
          return JsonResponse({'message':'BookRecord_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status = 400)
    
    @LoginAccess
    def put(self, request):
        try:
            data                 = json.loads(request.body)
            accountbookrecord_id = data['record_id']

            accountbookrecord    = AccountBookRecord.objects.get(
              user_id            = request.user.id,
              id                 = accountbookrecord_id
            )

            accountbookrecord.amount = data['amount']
            accountbookrecord.memo   = data['memo']
            accountbookrecord.save()
            
            return JsonResponse({'message':'CHANGE', 'CHANGE_AMOUNT': accountbookrecord.amount, 'CHANGE_MEMO': accountbookrecord.memo}, status = 200)

        except AccountBookRecord.DoesNotExist :
          return JsonResponse({'message': 'BookRecord_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status = 400)

class AccountBookRecordDataCopyView(View):
    @LoginAccess
    def post(self, request):
        try:
            data                = json.loads(request.POST.get('data'))
            title               = data.get('title')
            date                = data.get('date')
            memo                = data.get('memo')
            description         = data.get('description')
            amount              = data.get('amount')
            balance             = data.get('balance')
            serial_no           = data.get('serial_no')
            account_book_id     = data.get('book_id')
            user                = request.user

            AccountBookRecord.objects.create(
                title           = title,
                date            = date,
                memo            = memo,
                description     = description,
                amount          = amount,
                balance         = balance,
                serial_no       = serial_no,
                account_book_id = account_book_id,
                user            = user

            ) 

            return JsonResponse({"message":"SUCCESS"},status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
        except AccountBookRecord.DoesNotExist:
            return JsonResponse({"message":"BookRecord_DoesNotExist"}, status = 400)

