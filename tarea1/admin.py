from django.contrib import admin
from .models import Valores, Jurisprudencias


class AdminValores(admin.ModelAdmin):
    list_display = ('id_valores', 'id_jurisprudencia','id_parametro', 'id_item_lista',
                    'valor', 'parametro', 'item')


class AdminJurisprudencias(admin.ModelAdmin):
    list_display = ('id_jurisprudencia', 'tipo_causa', 'rol', 'caratula',
                    'nombre_proyecto', 'fecha_sentencia',
                    'descriptores','link_sentencia', 'url_sentencia',
                    'activo','tribunal', 'tipo', 'relacionada', 'visitas')


admin.site.register(Valores, AdminValores)
admin.site.register(Jurisprudencias, AdminJurisprudencias)
