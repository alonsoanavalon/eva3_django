from django import forms
from administracion.models import User
from administracion.models import Consulta
from administracion.models import Respuesta

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = '__all__'


class ConsultaForm(forms.ModelForm):
    class Meta:
        model= Consulta
        fields = '__all__'

class RespuestaForm(forms.ModelForm):
    class Meta:
        model= Respuesta
        fields = '__all__'

        
