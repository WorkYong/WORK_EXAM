import re, jwt, bcrypt

import pyshorteners as ps

from functools           import wraps
from django.conf         import settings
from django.http         import JsonResponse

from users.models        import User
from accountbooks.models import AccountBook

'''
api에 필요한 유틸리티를 함수화하여 보관하였습니다.

이유는 코드의 가독성을 높이고 재활용 하기 위해서입니다.

'''

'''
유효성검사

'''

def vaildNameRegex(value):
    REGEX_NAME     = '^[가-힣]{2,5}$'
    if not re.match(REGEX_NAME, value):
        raise ValueError("VAILDAITION_NAME_ERROR")

def validPasswordRegex(value):
    REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[?!@#$%*&])[A-Za-z\d?!@#$%*&]{8,}$'
    if not re.match(REGEX_PASSWORD, value):
        raise ValueError("VAILDAITION_PASSWORD_ERROR")

def validEmailRegex(value):
    REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(REGEX_EMAIL, value):
        raise ValueError("VAILDAITION_EMAIL_ERROR")

def validPhoneNumberRegex(value):
    REGEX_PHONE_NUMBER   = '^\d{3}-\d{3,4}-\d{4}$'
    if not re.match(REGEX_PHONE_NUMBER, value):
        raise ValueError("VAILDAITION_PHONE_NUMBER_ERROR")

def hash(value):
    hashed = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    return hashed

def checkPassword(incomePw, recordedPw):
    encoded_password = incomePw.encode('utf-8')
    user_password    = recordedPw.encode('utf-8')
    if not bcrypt.checkpw(encoded_password, user_password):
        raise ValueError("INVALID_EMAIL OR INVALID_PASSWORD")

def createToken(value):
    token = jwt.encode({'id': value}, settings.SECRET_KEY, settings.ALGORITHM)
    return token

def checkEmailExist(value):
    if User.objects.filter(email = value).exists():
        raise ValueError("EXIST_EMAIL")

def checkPhoneExist(value):
    if User.objects.filter(phone_number = value).exists():
        raise ValueError("EXIST_PHONE_NUMBER")
        
def checkBookNameExist(value):
    if AccountBook.objects.filter(book_name = value).exists():
        raise ValueError("EXIST_BOOK_NAME")

'''
로그인 검증
'''

def LoginAccess(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            user         = User.objects.get(id = payload['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID TOKEN'}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID USER'}, status = 400)
        return func(self, request, *args, **kwargs)

    return wrapper

'''
단축url 만들기
'''

def shortUrl(value1, value2, value3):

    book_id    = value1
    serial_no  = value2
    is_deleted = value3
    
    link       = f'localhost:8000/accountbookrecord?book_id={book_id}&serial_no={serial_no}&is_delted={is_deleted}'
    sh         = ps.Shortener()
    short_url  = (sh.tinyurl.short(link))
    
    return short_url