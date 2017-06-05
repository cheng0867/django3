from django.shortcuts import render
from models import *
# Create your views here.

def login(request):
    context = {

    }
    return render(request,'df_user/login.html',context)

def register(request):
    context = {

    }
    return render(request,'df_user/register',context)