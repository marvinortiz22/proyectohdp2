from django.shortcuts import get_object_or_404, render, redirect
from gestionAccidentes.models import DatosExtra, ReporteAccidente, Reporte
from .forms import AccidenteForm, DatosExtraForm, FiltroForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def IniciarSesion(request):
    form=AuthenticationForm()
    return render(request, "IniciarSesion.html",{"form":form})

def Registrarse(request):
    form=UserCreationForm()
    return render(request, "Registrarse.html",{"form":form})

def bienvenida(request):

    return render(request,"inicio.html")

def listaDeAccidentes(request):
    
    if request.method=="POST":
        filtro=FiltroForm(request.POST)
        if filtro.filtrar_por.value()=="Departamento":
            accidentes=ReporteAccidente.objects.filter(departamento=filtro.filtro.value())
            reportes=Reporte.objects.all()
            filtro=FiltroForm() 
    else:
        accidentes=ReporteAccidente.objects.all()
        reportes=Reporte.objects.all()    
        filtro=FiltroForm()
    return render(request,"listaDeAccidentes.html",{"accidentes":accidentes, "reportes":reportes, "filtro":filtro})

def registrarAccidente(request):
    if request.method=="POST":
        accidente=ReporteAccidente()
        form=AccidenteForm(request.POST)
        datosExtra=DatosExtra()
        form2=DatosExtraForm(request.POST, request.FILES)
        if form.is_valid():
            accidente=form.save(commit=False)
            accidente.user=request.user
            accidente.save()
            datosExtra=form2.save(commit=False)
            datosExtra.accidente=accidente
            datosExtra.save()
            return redirect('listaDeAccidentes')
    else:
        form=AccidenteForm()
        form2=DatosExtraForm()
    return render(request,"registrarAccidente.html", {'form':form,'form2':form2})

def Detalles(request, id):
    accidente=get_object_or_404(ReporteAccidente, id=id)
    
    form=AccidenteForm(instance=accidente)
    detalles=DatosExtra.objects.filter(accidente=accidente).first()
    if detalles:
        form2=DatosExtraForm(instance=detalles)
    else:
        form2=DatosExtraForm()
    return render(request, "detalles.html",{"form":form, "form2":form2, "detalles":detalles})

def reportar(request, id):
    accidente=get_object_or_404(ReporteAccidente, id=id)
    reporteExiste=Reporte.objects.filter(accidente=accidente, user=request.user)
    if(reporteExiste):
        return redirect('listaDeAccidentes')
    else:
        reporte=Reporte()
        reporte.accidente=accidente
        reporte.user=request.user
        reporte.save()
        return  redirect('listaDeAccidentes')

def cerrarSesion(request):
    return 
