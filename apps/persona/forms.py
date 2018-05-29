from django.forms import ModelForm
from apps.persona.models import User
class Insert_client (ModelForm):
    class Meta:
        model=User
        fields='__all__'
