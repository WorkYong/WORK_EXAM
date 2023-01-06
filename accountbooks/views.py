import json

from json.decoder         import JSONDecodeError

from django.http          import JsonResponse
from django.views         import View
from django.utils         import timezone

from accountbooks.models  import AccountBook
from core.utils           import LoginAccess , checkBookNameExist

class AccountBookView(View):
    @LoginAccess
    def post(self, request):
        try:
            data      = json.loads(request.body)
            user_id   = request.user.id
            book_name = data['book_name']

            checkBookNameExist(book_name)

            AccountBook.objects.create(
            book_name = book_name,
            user_id   = user_id
            )
            return JsonResponse({'message':'SUCCESS'}, status = 201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
    
    @LoginAccess
    def get(self, request):
        accountbooks = AccountBook.objects.filter(user=request.user)
        
        result = [
        {
          'id'        : accountbook.id,
          'book_name' : accountbook.book_name,
          'is_deleted': accountbook.is_deleted,
          'created_at': accountbook.created_at,
          'updated_at': accountbook.updated_at,
          
        } for accountbook in accountbooks]
          
        return JsonResponse({"result":result}, status = 200)

    @LoginAccess
    def patch(self, request):
        try:
            data           = json.loads(request.body)
            accountbook_id = data['book_id']
            is_deleted     = False
            
            accountbooks   = AccountBook.objects.get(
              id           = accountbook_id, 
              user_id      = request.user.id)

            if is_deleted == False :
              accountbooks.is_deleted = False
              accountbooks.deleted_at = timezone.now()
              accountbooks.save()
              
              return JsonResponse({'message':'DELETE', 'is_deleted': accountbooks.is_deleted,  'deleted_at':accountbooks.deleted_at}, status = 200)
            else :
              return JsonResponse({'message':"BAD REQUEST"}, status = 400) 

        except AccountBook.DoesNotExist :
          return JsonResponse({'message':'Book_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status = 400)
    
    @LoginAccess
    def put(self, request):
        try:
            data           = json.loads(request.body)
            accountbook_id = data['book_id']

            accountbooks   = AccountBook.objects.get(
              user_id      = request.user.id,
              id           = accountbook_id
            )

            accountbooks.book_name = data ['book_name']
            accountbooks.save()
            
            return JsonResponse({'message':'CHANGE', 'change_book_name': accountbooks.book_name}, status = 200)

        except AccountBook.DoesNotExist :
          return JsonResponse({'message':'Book_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status = 400)
    

