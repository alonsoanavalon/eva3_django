from django.shortcuts import render, redirect
from django.http import HttpResponse
from online.models import User
from online.forms import UserForm
from online.models import Consulta
from online.forms import ConsultaForm
from online.models import Respuesta
from online.forms import RespuestaForm
from online.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# Create your views here.
 
from . import forms
 
def renderAdmin(request):
   respuestas= Respuesta.objects.all()
   consultas = Consulta.objects.all()
   
   data = {
        'respuestas': respuestas,
        'consultas': consultas
    }
   return render(request, 'administracion.html', data)

def login_page(request):
    return render(request, 'login.html', {'form': LoginForm})


@csrf_exempt 
def ingresar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            datos = request.POST.dict()
            try:
                is_logged = User.objects.get(user=datos['user'])
                if is_logged:
                    if is_logged.password == datos['password']:
                        if is_logged.rol == "ADMINISTRADOR":
                            return redirect('/administracion')   
                        else:
                            return redirect('/usuarios')                     
                    else:
                        return redirect('/')
                else:
                    return redirect('/')
            except User.DoesNotExist:
                return redirect('/')
        else: 
            return redirect('/')
    else:
        return redirect('/')
    
 
def agregarComuna(request):
   form=forms.ComunaForm()
   if request.method == 'POST':
       form = ComunaForm(request.POST)
       if form.is_valid():
           form.save()
       return listadoComunas(request)
   data = {'form' : form}
   return data
 
def quitarComuna(request, id):
   comuna= Comuna.objects.get(id=id)
   comuna.delete()
   return redirect("/comunas")
  
 
def cambiarComuna(request, id):
   comuna= Comuna.objects.get(id=id)
   form= ComunaForm(instance=comuna)
   if request.method == 'POST':
       form= ComunaForm(request.POST, instance= comuna)
       if form.is_valid():
           form.save()
       return listadoComunas(request)
   data = {'form': form}
   return render(request, 'agregarcomunas.html', data)
 
def buscarComuna(request, id):
   comuna= Comuna.objects.get(id=id)
   data= {'comunas': comuna}
   return render(request, 'comunas.html',data)