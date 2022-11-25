from django import forms
from online.models import User
from online.models import Consulta
from online.models import Respuesta
 
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

class LoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields = [
            "user",
            "password"
        ]

        

