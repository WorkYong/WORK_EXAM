import json

from json          import JSONDecodeError

from django.http   import JsonResponse
from django.views  import View

from users.models  import User
from core.utils    import *

'''회원가입'''
class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            '''
            유효성검사, 및 토큰생성 등은 전부 core라는 폴더안에 모아서 함수화 처리 했습니다.
            그 이유는 코드의 가독성을 높이고 어디서든 재활용하기 위해서 입니다.
            비밀번호는 bcrypt 모듈을 통하여 진행했습니다.
            '''
            
            vaildNameRegex(name)
            validEmailRegex(email)
            validPasswordRegex(password)
            validPhoneNumberRegex(phone_number)
            checkEmailExist(email)
            checkPhoneExist(phone_number)

            User.objects.create(
                name         = name,
                email        = email,
                password     = hash(password),
                phone_number = phone_number,

            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

'''
로그인view 로그인 성공시 access_token을 발행합니다.

'''            
class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            checkPassword(password, user.password)
            return JsonResponse({'message':'SUCCESS', 'access_token':createToken(user.id), 'name':user.name}, status=201)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

        except ValueError:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'message':'User_DoesNotExist'}, status = 404)

'''
회원 탈퇴
클라이언트로 부터 user_id값을 요청 받습니다.
그 요청받은 user_id는 상태 값(is_active)를 False로 변환하여줍니다(기본값은 True)
그래서 False 처리 된 회원은 비식별 탈퇴 처리됩니다.
'''

class UserView(View):
    @LoginAccess
    def patch(self, request):
        try:
            data            = json.loads(request.body)
            user_id         = data['user_id']
            
            users = User.objects.get(id = user_id) 
          
            users.is_active = False
            users.save()
            
            return JsonResponse({'message':'DELETED'}, status = 200)

        except User.DoesNotExist :
          return JsonResponse({'message':'User_DoesNotExist'}, status = 400)
        except JSONDecodeError :
          return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
        except KeyError:
          return JsonResponse({'message':'KEY_ERROR'}, status = 400)