from django.urls import path

from .views import AccountBookRecordView
urlpatterns = [
    path('', AccountBookRecordView.as_view()),
]
