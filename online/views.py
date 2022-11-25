from django.shortcuts import render, redirect
from django.http import HttpResponse
from online.models import User
from online.forms import UserForm
from online.models import Consulta
from online.forms import ConsultaForm
from online.models import Respuesta
from online.forms import RespuestaForm
from online.forms import LoginForm
from online.forms import GenerarRespuestaForm
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
                        elif is_logger.rol == "TECNICO":
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
    
def listadoConsultas(request):
   consultas= Consulta.objects.all()
   data = {'consultas':consultas}
   return render(request, 'consultas.html', data)


def agregarConsulta(request):
   form=forms.ConsultaForm()
   if request.method == 'POST':
       form = ConsultaForm(request.POST)
       if form.is_valid():
           form.save()
       return listadoConsultas(request)
   data = {'form' : form}
   return render(request, 'agregarConsultas.html', data )

def login_page(request):
    return render(request, 'login.html', {'form': LoginForm})

def generarRespuesta(request, id):
    return render(request, 'agregarRespuestas.html', {'form': GenerarRespuestaForm, 'consulta_id': id})

def guardarRespuesta(request, id):
    print(request)
    respuesta = request.POST.dict()
    respuestaFormat = {}
    form = forms.RespuestaForm()
    if request.method == 'POST':
        if respuesta:
            respuesta['tecnico']
            respuesta['respuesta']
            respuesta['id_consulta'] = id
            form = RespuestaForm(respuesta)
            if form.is_valid():
                form.save()
                return redirect('/administracion')
            else:
                return redirect('/')
    return redirect('/')
    


 
def quitarConsulta(request, id):
   consulta= Consulta.objects.get(id=id)
   consulta.delete()
   return redirect("/administracion")
  
 
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