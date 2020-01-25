from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Ticket(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    srtid = models.CharField(max_length = 30)
    srtpw = models.CharField(max_length = 30)
    logintype = models.CharField(max_length = 30)

    dpt = models.CharField(max_length = 30)
    arr = models.CharField(max_length = 30)
    adult = models.CharField(max_length = 30)
    child = models.CharField(max_length = 30)
    date = models.CharField(max_length = 30)

    dptime = models.CharField(max_length = 30)
    ticketnum = models.CharField(max_length = 30)
    is_complete = models.BooleanField(default=False)

    phone = models.CharField(max_length = 30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) +' : '+ self.phone

    class Meta:
        ordering = ["-id"]