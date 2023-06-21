from django.contrib import admin
from tarea2.models import ConcesionesMaritimas


class AdminConcesionesMaritimas(admin.ModelAdmin):
    list_display = ('n', 'n_concesion', 'tipo_concesion', 'comuna',
                    'lugar', 'n_rs_ds', 'tipo_tramite',
                    'concesionario', 'tipo_vigencia')


admin.site.register(ConcesionesMaritimas, AdminConcesionesMaritimas)
