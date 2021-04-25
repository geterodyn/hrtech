from django.urls import path
from .views import PollingList, PollingDetail, PollingExec, PollingResult

app_name = 'polls'

urlpatterns = [
    path('', PollingList.as_view(), name='list'),
    path('<slug:slug>/', PollingDetail.as_view(), name='detail'),
    path('<slug:slug>/execute/<int:pk>/', PollingExec.as_view(), name='execute'),
    path('<slug:slug>/result/<int:pk>/', PollingResult.as_view(), name='result')
]