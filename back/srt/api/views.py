from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from time import sleep
from .tasks import srt


@api_view(['GET'])
def index(request, pk):
    qs = Ticket.objects.get(pk=pk)
    serializer = TicketSerializer(qs)
    srt(serializer.data)
    return Response(serializer.data)

    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]


