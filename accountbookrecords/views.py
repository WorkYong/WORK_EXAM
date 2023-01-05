import json
from json.decoder         import JSONDecodeError

from django.http          import JsonResponse
from django.views         import View

from accountbookrecords.models  import AccountBookRecord
from core.utils           import LoginAccess 

class AccountBookRecordView(View):
    @LoginAccess
    def post(self, request):
        try:
            data            = json.loads(request.body)
            title           = data['title'],
            date            = data['date'],
            memo            = data['memo'],
            description     = data['description'],
            amount          = data['amount'],
            balance         = data ['balance'],
            account_book_id = data ['accountbook_id']
            user_id         = request.user.id

            AccountBookRecord.objects.create(
              title           = title,
              date            = date,
              memo            = memo,
              description     = description,
              amount          = amount,
              balance         = balance,
              user_id         = user_id,
              account_book_id = account_book_id

            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
    
    @LoginAccess
    def get(self, request):
        
        accountbookrecords = AccountBookRecord.objects.filter(user=request.user)
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
          
        return JsonResponse({"result":result}, status = 200)

    @LoginAccess
    def patch(self, request):
        try:
            data           = json.loads(request.body)
            accountbook_id = data['accountbook_id']

            accountbooks = AccountBook.objects.get(
              id = accountbook_id, 
              user_id = request.user.id)

            accountbooks.is_deleted = data['is_deleted']
            accountbooks.deleted_at = data['deleted_at']
            accountbooks.save()

            return JsonResponse({'is_deleted': accountbooks.is_deleted, 'deleted_at':accountbooks.deleted_at}, status = 200)

        except AccountBook.DoesNotExist :
          return JsonResponse({'message': 'Book_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status=400)
    
    @LoginAccess
    def put(self, request):
        try:
            data           = json.loads(request.body)
            accountbook_id = data['accountbook_id']

            accountbooks   = AccountBook.objects.get(
              user_id      = request.user.id,
              id           = accountbook_id
            )

            accountbooks.book_name = data ['book_name']
            accountbooks.save()
            
            return JsonResponse({'change_book_name': accountbooks.book_name}, status = 200)

        except AccountBook.DoesNotExist :
          return JsonResponse({'message': 'Book_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status=400)
    

