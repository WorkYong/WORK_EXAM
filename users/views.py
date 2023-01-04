import json

from django.http   import JsonResponse ,HttpResponseRedirect
from django.views  import View

from users.models  import User
from core.utils import *

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

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
            
class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            checkPassword(password, user.password)
            return JsonResponse({'message': 'SUCCESS', 'access_token': createToken(user.id), 'name': user.name}, status=201)
            
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'User_DoseNotExist'}, status=404)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)