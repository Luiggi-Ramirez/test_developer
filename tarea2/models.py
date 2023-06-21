from django.db import models

class ConcesionesMaritimas(models.Model):
    """Model para guardar las concesiones"""
    n = models.CharField(max_length=10, primary_key=True)
    n_concesion = models.CharField(max_length=10)
    tipo_concesion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=20)
    lugar = models.CharField(max_length=120)
    n_rs_ds = models.CharField(max_length=20)
    tipo_tramite = models.CharField(max_length=120)
    concesionario = models.CharField(max_length=120)
    tipo_vigencia = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"""N: {self.n}
                - N Consecion: {self.n_concesion}
                - Tipo Concesion: {self.tipo_concesion}
                - Comuna: {self.comuna}
                - Lugar: {self.lugar}
                - N RS DS: {self.n_rs_ds}
                - Tipo tramite: {self.tipo_tramite}
                - Concesionario: {self.concesionario}
                - Tipo Vigencia: {self.tipo_vigencia}"""
