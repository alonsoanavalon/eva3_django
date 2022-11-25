from django.shortcuts import render, redirect
from django.http import HttpResponse
from online.models import User
from online.forms import UserForm
from online.models import Consulta
from online.forms import ConsultaForm
from online.models import Respuesta
from online.forms import RespuestaForm
 
# Create your views here.
 
from . import forms
 
def listadoUsers(request):
   users= User.objects.all()
   data = {'users':users}
   return render(request, 'users.html', data)
 
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