from django.shortcuts import render
from apps.mark.models import Mark
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.views.generic import  UpdateView,DeleteView,ListView
from django.views.generic.edit import FormView
from apps.mark.forms import form_marks
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class view_marks (ListView):
    model=Mark
    template_name='Marks/view_marks.html'

class Create_marks (FormView):
    template_name='Marks/create_mark.html'
    form_class=form_marks
    success_url=reverse_lazy('view_marks')
    def form_valid (self,form):
        form.save()
        return super().form_valid(form)

    @method_decorator(permission_required('Mark.add_Mark',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(Create_marks,self).dispatch(*args,**kwargs)

class Edit_marks (UpdateView):
    model=Mark
    template_name='Marks/create_mark.html'
    form_class=form_marks
    success_url=reverse_lazy('view_marks')
    @method_decorator(permission_required('Mark.add_Mark',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(Edit_marks,self).dispatch(*args,**kwargs)

class remove_mark (DeleteView):
    model=Mark
    template_name='Marks/remove_mark.html'
    success_url=reverse_lazy('view_marks')
    @method_decorator(permission_required('Mark.add_Mark',reverse_lazy('permission')))
    def dispatch(self,*args,**kwargs):
        return super(remove_mark,self).dispatch(*args,**kwargs)
