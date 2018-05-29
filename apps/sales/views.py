from django.views.generic.edit import FormView
from apps.sales.forms import Insert_Sales
from django.urls import reverse_lazy,reverse
from apps.sales.models import Sale
from apps.instruments.models import Instruments
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from apps.sales.models import Sale
from django.db.models import Sum
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.views.generic import View


class Create_sales (FormView):

	template_name='Sales/insert_sales.html'
	form_class=Insert_Sales
	success_url=reverse_lazy('instrument')
	def form_valid(self,form):
		form.save()
		S=Sale.objects.latest("id")
		S.Price_sale=Instruments.objects.filter(sale__id=S.id).aggregate(Sum('Price'))['Price__sum']
		S.save()
		return super().form_valid(form)

class sales (ListView):
	model=Sale
	template_name='Sales/sales.html'

	@method_decorator(permission_required('Sale.add_Sale',reverse_lazy('permission')))
	def dispatch (self,*args,**kwargs):
		return super(sales,self).dispatch(*args,**kwargs)




def most_sold (request):
	I=Instruments.objects.all()
	for i in I:
		Q=Sale.objects.filter(id_sale_Instrument=i.ID)
		i.Quantity=Q.count()
		i.Production=i.Price*Q.count()
		i.save()
	context={'elements':I}
	return render(request,'Sales/max_sold.html',context)



# def view_sales (request):
# 	sales=Sale.objects.all()
# 	context={'sales':sales}
# 	return render(request,'Sales/sales.html',context)

def sell_intruments (request,pk):
	I=Instruments.objects.get(ID=pk)
	number_sales=Sale.objects.count()
	if I.Quantity > 0:
		s=Sale(Model_instrument=I.Model,Price_sale=I.Price,id_sale_Instrument=I)
		I.Quantity-=1
		I.save()
		s.save()
		sales=Sale.objects.all()
		context={'sales':sales,'number_sales':number_sales}
		return HttpResponseRedirect(reverse('saleview'))
	else:
		return HttpResponseRedirect(reverse('saleview'))
def info_sell (request,pk):

	sales=Sale.objects.filter(id=pk)
	context={'sales':sales}
	return render(request,'Sales/info_sell.html',context)

def order (request):
	I=Instruments.objects.order_by('Quantity').reverse()
	context={'elements':I}
	return render(request,'Sales/max_sold.html',context)
def order_asc (request):
	I=Instruments.objects.order_by('Quantity')
	context={'elements':I}
	return render(request,'Sales/max_sold.html',context)

class search_Sale (TemplateView):
	def post (self,request,*args,**kwargs):
		try:
			search=request.POST['Sales']
			sales=Sale.objects.filter(Date_sale=search)
			context={'sales':sales}
			return render(request,'Sales/sales2.html',context)
		except:
			return render(request,'Sales/sales.html')
