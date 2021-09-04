from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime
from login.models import *
import bcrypt



# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def registrar(request):
    return render(request, 'login/registro.html')

def inicio(request):
    usuario = User.objects.filter(email=request.POST['email'])
    errores = User.objects.validar_login(request.POST, usuario)
    employee=Employee.objects.all()


    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['id'] = usuario[0].id
        return redirect('home/')

def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')
        #crear usuario
        if request.POST['rol'] == '1':
            user = User.objects.create(
                name=request.POST['name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=1,
            )
        else:
            user = User.objects.create(
                name=request.POST['name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=2,
            )
        request.session['id'] = user.id
    return redirect('home/')

def logout(request):
    request.session.flush()
    return redirect('/')