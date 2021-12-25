from django.shortcuts import render
from django.http import HttpResponse
from django.views import  View
from .models import  Admin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit  import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class  AdminCreate(CreateView):
    model = Admin
    fields = ["id","username","last_name","password","email","mobile_no"]
    success_url="viewadmin"

class Adminlist(ListView):
    model = Admin

class Detail(DetailView):
    model = Admin

class Updatedetail(UpdateView):
    model = Admin
    fields =["id","username","last_name","password","email","mobile_no"]
    success_url= "/viewadmin"

class Deletedata(DeleteView):
     model = Admin
     success_url= "/viewadmin"

