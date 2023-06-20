from django.utils import dateparse
from rest_framework.views import APIView
from rest_framework.response import Response

from tarea1.models import Valores, Jurisprudencias
from tarea1.consume_api import get_jurisprudences


class ViewJurisprudencias(APIView):
    def get(self, request):
        search = request.query_params.get('search')
        payload = {"page": 1, "pageSize": 10, "search": search, "orden": "nuevo"}
        # Obtengo un listado de jurisprudencias en base a la búsqueda
        data = get_jurisprudences(payload)
        if data != []:
            for dt in data:
                lst_jurisprudencias = [Jurisprudencias(
                    id=dt['id'],
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
                    )]
                # Guardamos los datos de las jurisprudencias
                j = Jurisprudencias.objects.bulk_create(lst_jurisprudencias,
                ignore_conflicts=True)

                for v in dt['valores']:
                    lst_valores = [Valores(
                        id=v['id'],
                        jurisprudencia=j[0],
                        id_parametro=v['idParametro'],
                        id_item_lista=v['idItemlista'],
                        valor=v['valor'],
                        parametro=v['parametro'],
                        item=v['item']
                    )]
                    #Guardamos los valores asociados a una jurisprudencia
                    Valores.objects.bulk_create(lst_valores, ignore_conflicts=True)
            #Retornamos un json con la data que devuelve la request
            return Response({"msg": data})
        return Response({})
