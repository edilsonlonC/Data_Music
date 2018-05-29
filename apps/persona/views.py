from django.shortcuts import render
from django.views.generic import  UpdateView,DeleteView,ListView
from django.views.generic.edit import FormView
from apps.persona.forms import Insert_client
from apps.persona.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
class create_clients (FormView):
    template_name='Clients/create_clients.html'
    form_class=Insert_client
    success_url=reverse_lazy('view_clients')
    def form_valid (self,form):
        form.save()
        return super().form_valid(form)

    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch (self,*args,**kwargs):
        return super(create_clients,self).dispatch(*args,**kwargs)

class view_clients (ListView):
    model=User
    template_name='Clients/view_clients.html'
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch (self,*args,**kwargs):
        return super(view_clients,self).dispatch(*args,**kwargs)

class Remove_client (DeleteView):
    model=User
    template_name='Clients/remove_client.html'
    success_url=reverse_lazy('view_clients')
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch (self,*args,**kwargs):
        return super(Remove_client,self).dispatch(*args,**kwargs)


class Edit_client (UpdateView):
    model=User
    template_name='Clients/create_clients.html'
    form_class=Insert_client
    success_url=reverse_lazy('view_clients')
    @method_decorator(permission_required('User.add_User',reverse_lazy('permission')))
    def dispatch (self,*args,**kwargs):
        return super(Edit_client,self).dispatch(*args,**kwargs)
