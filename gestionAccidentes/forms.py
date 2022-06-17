from django import forms
from .choices import Departamentos, Filtros
from .models import DatosExtra, ReporteAccidente
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class AccidenteForm(forms.ModelForm):
    descripcion=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':'3'}))
    departamento=forms.ChoiceField(choices=Departamentos)
    class Meta:
        model=ReporteAccidente
        exclude=['user']

class DatosExtraForm(forms.ModelForm):
    class Meta:
        model=DatosExtra
        exclude=['accidente']
      
class FiltroForm(forms.Form):
    filtrar_por=forms.ChoiceField(choices=Filtros)
    filtro=forms.CharField()

class loginForm(AuthenticationForm):
    username=forms.IntegerField()
    password: forms.CharField()
    class Meta:
        fields='__all__'

class RegistroForm(UserCreationForm):
    username=forms.IntegerField()
    class Meta:
        model=User
        fields=['username','password1','password2']