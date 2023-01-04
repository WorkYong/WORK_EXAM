import json

from django.http   import JsonResponse
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

            User.objects.create(
                name         = name,
                email        = email,
                password     = hash(password),
                phone_number = phone_number,

            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
