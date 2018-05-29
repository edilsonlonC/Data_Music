from django.forms import ModelForm
from apps.mark.models import Mark

class form_marks (ModelForm):

    class Meta:
        model=Mark
        fields='__all__'
