from django.urls import path
from rest_framework import routers
from .views import TicketViewSet, index



router = routers.DefaultRouter()
router.register('ticket', TicketViewSet) #티켓팅에 필요한 항목만 받기위한 뷰셋

urlpatterns =[
    path('ticketing/<int:pk>', index),
]

urlpatterns += router.urls
