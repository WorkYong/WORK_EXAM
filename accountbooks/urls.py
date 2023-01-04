from django.urls import path

from .views import AccountBookView
urlpatterns = [
    path('', AccountBookView.as_view()),
]
