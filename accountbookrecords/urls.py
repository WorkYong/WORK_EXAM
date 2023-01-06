from django.urls import path

from .views import AccountBookRecordView, AccountBookRecordDataCopyView
urlpatterns = [
    path('', AccountBookRecordView.as_view()),
    path('/copy', AccountBookRecordDataCopyView.as_view())
]
