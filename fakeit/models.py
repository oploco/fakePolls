from django.db import models

class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=15)
    fundacion = models.DateField()
    color_primario = models.CharField(max_length=7)
    color_secundario = models.CharField(max_length=7)

    class Meta:
        db_table = 'partidopolitico'
        db_table_comment = 'Tabla para los partidos'

    def __str__(self):
        return self.nombre

class VotosPorAnio(models.Model):
    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    anio = models.PositiveIntegerField()
    cantidad_votos = models.PositiveIntegerField()

    class Meta:
        db_table = 'votosporanio'
        db_table_comment = 'Tabla para los votos por partidos'

    def __str__(self):
        return f"{self.partido} - {self.anio}: {self.cantidad_votos} votos"
