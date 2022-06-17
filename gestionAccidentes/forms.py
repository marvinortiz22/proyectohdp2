from django import forms
from .choices import Departamentos, Filtros
from .models import DatosExtra, ReporteAccidente

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

