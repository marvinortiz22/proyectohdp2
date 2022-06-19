"""ProyectoHDP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionAccidentes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name="inicio"),
    path('listaDeAccidentes/',views.listaDeAccidentes, name="listaDeAccidentes"),
    path('registrarAccidente/',views.registrarAccidente, name="registrarAccidente"),
    path('Detalles/<id>',views.Detalles,name="detalles"),
    path('reportar/<id>',views.reportar, name="reportar"),
    path('accounts/login/',views.IniciarSesion, name="IniciarSesion"),
    path('Registrarse/',views.Registrarse, name="Registrarse"),
    path('cerrarSesion/',views.cerrarSesion, name="cerrarSesion"),
]
urlpatterns +=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)