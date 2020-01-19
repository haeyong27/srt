from django.db import models
from django.conf import settings


class Ticket(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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