from django.contrib import admin
from .models import Reporte, DatosExtra, ReporteAccidente


admin.site.register(Reporte)
admin.site.register(ReporteAccidente)
admin.site.register(DatosExtra)
# Register your models here.
