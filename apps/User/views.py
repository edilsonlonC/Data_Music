from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from apps.User.forms import register_form
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

# Create your views here.

class User_register (CreateView) :
    model = User
    template_name = "Users/user_register.html"
    form_class = register_form
    success_url=reverse_lazy('instrument')
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(User_register,self).dispatch(*args,**kwargs)

class view_users (ListView):
    model=User
    template_name = "Users/list_users.html"
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(view_users,self).dispatch(*args,**kwargs)


class Edit_users (UpdateView):
    model=User
    template_name = "Users/user_register.html"
    form_class=register_form
    success_url=reverse_lazy('view_users')
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(Edit_users,self).dispatch(*args,**kwargs)

class Remove_user (DeleteView):
    model=User
    template_name="Users/delete_user.html"
    success_url=reverse_lazy('view_users')
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(Remove_user,self).dispatch(*args,**kwargs)
