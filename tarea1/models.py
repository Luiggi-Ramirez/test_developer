from django.db import models


class Jurisprudencias(models.Model):
    '''Modelo para las Jurisprudencias'''
    id = models.BigIntegerField(primary_key=True)
    tipo_causa = models.CharField(max_length=20)
    rol = models.CharField(max_length=50)
    caratula = models.TextField()
    nombre_proyecto = models.TextField()
    fecha_sentencia = models.DateField(null=True, blank=True)
    descriptores = models.TextField(null=True, blank=True)
    link_sentencia = models.CharField(max_length=250)
    url_sentencia = models.URLField(max_length=250)
    activo = models.BooleanField(default=True)
    tribunal = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    relacionada = models.CharField(max_length=120, default="")
    visitas = models.IntegerField(default=0)


class Valores(models.Model):
    '''Modelo para los Valores ascoiados a una Jurisprudencia'''
    id = models.BigIntegerField(primary_key=True)
    jurisprudencia = models.ForeignKey(Jurisprudencias, on_delete=models.CASCADE)
    id_parametro = models.IntegerField()
    id_item_lista = models.IntegerField(null=True, blank=True)
    valor = models.TextField(null=True, blank=True)
    parametro = models.CharField(max_length=120)
    item = models.CharField(max_length=120, null=True, blank=True)
