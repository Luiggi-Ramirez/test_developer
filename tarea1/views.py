from django.views import View
from django.shortcuts import render
from django.utils import dateparse

from tarea1.models import Valores, Jurisprudencias
from tarea1.consume_api import get_jurisprudences


class ViewJurisprudencias(View):
    '''Vista que controla las Jurisprudencias'''
    def get(self, request, search):
        # search: la palabra a buscar
        payload = {"page": 1, "pageSize": 10, "search": search, "orden": "nuevo"}
        # Obtengo un listado de jurisprudencias en base a la búsqueda
        data = get_jurisprudences(payload)
        # Si la data no esta vacía podemos continuar
        if data != []:
            # Recorremos la data tomando cada diccionario
            for dt in data:
                # Creamos o actualizamos los datos de las jurispridencias en la db
                j = Jurisprudencias.objects.update_or_create(
                    id_jurisprudencia=dt['id'],
                    tipo_causa=dt['tipoCausa'],
                    rol=dt['rol'],
                    caratula=dt['caratula'],
                    nombre_proyecto=dt['nombreProyecto'],
                    fecha_sentencia=dateparse.parse_date(dt['fechaSentencia']),
                    descriptores=dt['descriptores'],
                    link_sentencia=dt['linkSentencia'],
                    url_sentencia=dt['urlSentencia'],
                    activo=dt['activo'],
                    tribunal=dt['tribunal'],
                    tipo=dt['tipo'],
                    relacionada=dt['relacionada'],
                    visitas=dt['visitas']
                )
                # Recorremos lo valores de la jurisprudencia
                for v in dt['valores']:
                    # Guardamos o actulizamos los datos de los valores en la db
                    Valores.objects.update_or_create(
                        id_valores=v['id'],
                        id_jurisprudencia=j[1],
                        id_parametro=v['idParametro'],
                        id_item_lista=v['idItemlista'],
                        valor=v['valor'],
                        parametro=v['parametro'],
                        item=v['item']
                    )
        # Retornamos el template con las jurisprudencias
        return render(request, 'jurisprudencia/jurisprudencia.html', context={"data": data})
