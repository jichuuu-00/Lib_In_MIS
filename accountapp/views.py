
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'accountapp/mem_login.html')

def login_mgr(request):
    return render(request, 'accountapp/mgr_login.html')

