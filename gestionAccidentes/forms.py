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
    cantVictimas=forms.IntegerField(min_value=0, label="Cantidad de victimas")
    class Meta:
        model=DatosExtra
        exclude=['accidente']
      
class FiltroForm(forms.Form):
    filtrar_por=forms.ChoiceField(choices=Filtros)
    filtro=forms.CharField()

class loginForm(AuthenticationForm):
    username=forms.CharField(label="DUI")
    password: forms.CharField()
    class Meta:
        fields='__all__'
   

class RegistroForm(UserCreationForm):
    username=forms.CharField(label="DUI")
    class Meta:
        model=User
        fields=['username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

