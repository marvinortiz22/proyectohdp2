from email import message
from django.shortcuts import get_object_or_404, render, redirect
from gestionAccidentes.models import DatosExtra, ReporteAccidente, Reporte
from .forms import AccidenteForm, DatosExtraForm, FiltroForm, loginForm, RegistroForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def IniciarSesion(request):
    if request.method=="POST":
        form=loginForm(request, data=request.POST)
        if form.is_valid():
            usuario=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if usuario:
                login(request, usuario) 
                return redirect('inicio')  
            else:
                for mensaje in form.error_messages:
                    messages.error(request, form.error_messages[mensaje])
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
    else:
        form=loginForm()
    return render(request, "IniciarSesion.html",{"form":form})

def Registrarse(request):
    if request.method=="POST":
        form=RegistroForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('inicio')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
    else:        
        form=RegistroForm()
    return render(request, "Registrarse.html",{"form":form})

@login_required
def inicio(request):

    return render(request,"inicio.html")

@login_required
def listaDeAccidentes(request):
    form=FiltroForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        if form.cleaned_data['filtrar_por']=="Departamento":
            accidentes=ReporteAccidente.objects.filter(departamento=form.cleaned_data['filtro']).order_by('-fecha')          
            form=FiltroForm()
        else:
            accidentes=ReporteAccidente.objects.filter(municipio=form.cleaned_data['filtro']).order_by('-fecha')          
            form=FiltroForm()
    else:
        accidentes=ReporteAccidente.objects.all().order_by('-fecha')
    return render(request,"listaDeAccidentes.html",{"accidentes":accidentes,  "filtro":form})

@login_required
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

@login_required
def Detalles(request, id):
    accidente=get_object_or_404(ReporteAccidente, id=id)
    
    form=AccidenteForm(instance=accidente)
    detalles=DatosExtra.objects.filter(accidente=accidente).first()
    if detalles:
        form2=DatosExtraForm(instance=detalles)
    else:
        form2=DatosExtraForm()
    return render(request, "detalles.html",{"form":form, "form2":form2, "detalles":detalles})

@login_required
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

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')
