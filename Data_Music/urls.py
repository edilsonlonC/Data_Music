"""Data_Music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.instruments.views import view_instruments,Insert_instrument,Update_instruments,remove_instruments,Home,Search,view_material,error_permission
from apps.User.views import User_register,view_users,Edit_users,Remove_user
from apps.sales.views import Create_sales,sell_intruments,search_Sale,info_sell,most_sold,order,order_asc,sales
from apps.mark.views import view_marks,Create_marks,Edit_marks,remove_mark
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import permission_required,login_required
from apps.persona.views import create_clients,view_clients,Edit_client,Remove_client
urlpatterns = [
    path('admin/', admin.site.urls),
    path('instruments/', login_required(view_instruments),name='instrument'),
    path('order/',  login_required(order),name='order'),
    path('order_asc/',  login_required(order_asc),name='order_asc'),
    path('sell/<int:pk>',  login_required(sell_intruments),name='sell'),
    path('info_sell/<int:pk>',  login_required(info_sell),name='info_sell'),
    path('max_sold/',  login_required(most_sold),name='max_sold'),
    #path('saleview/', view_sales,name='saleview'),
    path('material/',  login_required(view_material) ,name='material'),
    path('new/',  login_required(Insert_instrument.as_view()),name='new'),
    path('edit/<int:pk>', login_required(Update_instruments.as_view()),name='edit') ,
    path('remove/<int:pk>', login_required(remove_instruments.as_view()),name='remove') ,
    path('register/', login_required(User_register.as_view()),name='register') ,
    path('',login,{'template_name':'Users/index.html'},name='login'),
    path('logout',logout,{'next_page':'login'},name='logout'),
    path('home/',login_required(Home.as_view()),name='home'),
    path('search/', login_required(Search.as_view()),name='search') ,
    path('searchSales/', login_required(search_Sale.as_view()),name='searchSales') ,
    path('sales/', login_required(Create_sales.as_view()),name='sale') ,
    path('saleview/',  login_required(sales.as_view()),name='saleview'),
    path('view_users/',  login_required(view_users.as_view()),name='view_users'),
    path('update_user/<int:pk>', login_required(Edit_users.as_view()),name='update_user') ,
    path('remove_user/<int:pk>', login_required(Remove_user.as_view()),name='remove_user') ,
    path('permission/', error_permission.as_view(),name='permission'),
    path('view_marks/',  login_required(view_marks.as_view()),name='view_marks'),
    path('create_mark/',  login_required(Create_marks.as_view()),name='create_mark'),
    path('edit_mark/<int:pk>',  login_required(Edit_marks.as_view()),name='edit_mark'),
    path('remove_mark/<int:pk>',  login_required(remove_mark.as_view()),name='remove_mark'),
    path('create_clients/',  login_required(create_clients.as_view()),name='create_clients'),
    path('view_clients/',  login_required(view_clients.as_view()),name='view_clients'),
    path('edit_client/ <int:pk>',  login_required(Edit_client.as_view()),name='edit_client'),
    path('remove_client/ <int:pk>',  login_required(Remove_client.as_view()),name='remove_client'),


]
