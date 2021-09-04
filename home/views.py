from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from login.models import User
from home.models import *


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['id'])
    employees=Employee.objects.all()
    context = {
        "active_user": reg_user,
        'employees': employees,
    }

    return render(request, 'login/home.html', context)

def create(request):
    
    return redirect('/home/')


def read(request):
    return HttpResponse("read")



def update(request):
    return redirect('/home/')


def delete(request):
    #
    return redirect('/home/')


def employees(request):
    if 'id' in request.session:
        employees=Employee.objects.all()
        context = {
            'employees': employees,
        }
        return render(request, 'home/employees.html', context)
    else:
        return redirect('/')


def tools(request):
    pass

def moves(request):
    pass

def movetype(request):
    pass
