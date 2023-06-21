from django.views import View
from django.shortcuts import render

from tarea2.models import ConcesionesMaritimas
from tarea2.scraping import get_scraping_data, add_json_to_file

class ViewConcesiones(View):
    '''Vista para manegar las concesiones'''
    def get(self, request):
        # Obtener la data
        concesiones = get_scraping_data()
        # Crear el archivo json con la data
        add_json_to_file(concesiones)
        # Lista que almacena las concesiones
        lst_concesiones = []
        for concesion in concesiones:
            lst_concesiones.append(
                ConcesionesMaritimas(
                    n=concesion["n"],
                    n_concesion=concesion["n_concesion"],
                    tipo_concesion=concesion["tipo_concesion"],
                    comuna=concesion["comuna"],
                    lugar=concesion["lugar"],
                    n_rs_ds=concesion["n_rs_ds"],
                    tipo_tramite=concesion["tipo_tramite"],
                    concesionario=concesion["concesionario"],
                    tipo_vigencia=concesion["tipo_vigencia"]
                )
            )
        # Guardar los datos en la db
        ConcesionesMaritimas.objects.bulk_create(lst_concesiones, ignore_conflicts=True)
        # Retorno el render de la plantilla con las concesiones
        return render(request, 'scraping/scraping.html', context={'data': concesiones})
