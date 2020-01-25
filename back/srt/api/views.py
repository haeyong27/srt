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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            if not self.request.user.is_staff:
                qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs
