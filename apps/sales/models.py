from django.db import models
from django.conf import settings
from apps.instruments.models import Instruments
from django.db.models import Sum
from apps.persona.models import User

# Create your models here.


class Sale (models.Model):
    Date_sale=models.DateField(auto_now_add=True)
    time=models.DateTimeField(auto_now_add=True)
    id_sale_Instrument=models.ManyToManyField(Instruments)
    Price_sale=models.FloatField(default=0)
    Client=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
