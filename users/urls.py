from django.urls import path

from .views import SignUpView, LoginView, UserView
urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login',  LoginView.as_view()),
    path('/delete', UserView.as_view())
]