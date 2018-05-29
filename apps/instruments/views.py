from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from apps.instruments.models import Instruments,Material
from django.views.generic.edit import FormView
from django.views.generic import  UpdateView,DeleteView,ListView
from apps.instruments.forms import Insert_instruments
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required,login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth import logout
# Create your views here.
def view_instruments (request):
	instruments=Instruments.objects.all()
	context={'instruments':instruments}
	return render(request,'instruments/instruments.html',context)

def view_material (request):
	material=Material.objects.all()
	context={'material':material}
	return render (request,'instruments/search_material.html',context)

class Insert_instrument (FormView):
	template_name='instruments/form_instruments.html'
	form_class=Insert_instruments
	success_url=reverse_lazy('instrument')


	def form_valid(self,form):
		form.save()
		return super().form_valid(form)

	@method_decorator(permission_required('Instruments.add_Instruments',reverse_lazy('permission')))
	def dispatch (self,*args,**kwargs):
		return super(Insert_instrument,self).dispatch(*args,**kwargs)


class Update_instruments (UpdateView):
	model = Instruments
	template_name='instruments/form_instruments.html'
	form_class=Insert_instruments
	success_url=reverse_lazy('instrument')

	@method_decorator(permission_required('Instruments.add_Instruments',reverse_lazy('permission')))
	def dispatch(self,*args,**kwargs):
		return super(Update_instruments,self).dispatch(*args,**kwargs)

class remove_instruments (DeleteView):
	model=Instruments
	template_name='instruments/delete.html'
	success_url=reverse_lazy('instrument')
	@method_decorator(permission_required('Instruments.add_Instruments',reverse_lazy('permission')))
	def dispatch(self,*args,**kwargs):
		return super(remove_instruments,self).dispatch(*args,**kwargs)



class Home (TemplateView):
	template_name='Users/Home.html'



class Search1 (TemplateView):

	def post (self,request,*args,**kwargs):
		search=request.POST['Buscar'] # user input insert
		ins=Instruments.objects.filter(Id_Material__Material=search)
		if ins: # check if is a material
			instruments=ins
		else: # if is'n material is a instrument
			instruments=Instruments.objects.filter(Model__contains=search)
		context={'instruments':instruments}
		return render(request,'instruments/instruments.html',context)

class Search (TemplateView):

	def post (self,request,*args,**kwargs):
		search=request.POST['Buscar'] # user input insert
		ins=Instruments.objects.filter(Id_Material__Material=search)
		if ins: # check if is a material
			instruments=ins
		else: # if is'n material is a instrument
			ins=Instruments.objects.filter(Model__contains=search)
			if ins:
				instruments=ins

			else:
				instruments=Instruments.objects.filter(Id_Category__Type=search)
		context={'instruments':instruments}
		return render(request,'instruments/instruments.html',context)

class error_permission (TemplateView):
	template_name="errors/permission.html"
