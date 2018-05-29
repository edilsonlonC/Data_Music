from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class register_form (UserCreationForm):

    class Meta:
         model=User
        # fields='__all__'
         fields= [
         'username',
         'first_name',
         'last_name',
         'email',
         'is_superuser',
         ]
         labels= {
         'username' : 'Username',
         'first_name': 'first name',
         'last_name' : 'last name',
         'email': 'Email',
         'is_superuser': 'is Admin'
         }
