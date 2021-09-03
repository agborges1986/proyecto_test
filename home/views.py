from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from login.models import User


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['id'])

    context = {
        "active_user": reg_user,
    }

    return render(request, 'login/home.html', context)

def create(request):
    
    return redirect('/home/')


def read(request):
    return HttpResponse("read")


""" def getMove(request):
    
    context = {
        
    }
    return render(request,'home/edit.html', context) """


def update(request):
    return redirect('/home/')


def delete(request):
    #
    return redirect('/home/')


""" def generarPdf(request):
    servicios = Servicio.objects.all()
    context = {
        'titulo': "Lista de Servicios",
        "servicio": "",
        "object_list": servicios,
    }

    return render(request, 'home/listaServicios.html', context) """


""" class ServiciosListView(ListView):
    model = Servicio
    template_name = 'israel_palma/listaServicios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['titulo'] = "Lista de Servicios"
        return context """
