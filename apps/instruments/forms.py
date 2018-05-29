from django.forms import ModelForm
from django.forms import Textarea
from apps.instruments.models import Instruments

class Insert_instruments (ModelForm):
    class Meta:
        model=Instruments
        fields=[
        'ID',
        'Model',
        'Price',
        'Id_Category',
        'Id_Material',
        'id_Mark'
        ]

        labels={
        'ID':'id',
        'Model':'Model',
        'Price':'Price',
        'Id_Category':'Category',
        'Id_Material':'Material',
        'id_Mark':  'Mark',
        }
