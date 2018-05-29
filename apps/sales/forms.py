from django.forms import ModelForm
from django import forms
from django.forms import Textarea
from apps.sales.models import Sale
from apps.instruments.models import Instruments
from django.forms.widgets import CheckboxSelectMultiple
class Insert_Sales (ModelForm):
    id_sale_Instrument=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),queryset=Instruments.objects.all())
    class Meta:
        model=Sale
        fields='__all__'
        exclude=('Price_sale',)
