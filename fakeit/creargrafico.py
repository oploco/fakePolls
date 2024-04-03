import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import numpy as np
import pandas as pd
import os

from .models import PartidoPolitico,VotosPorAnio

class grafico:
    def creargrafico():
        """Para dibujo"""
        partidos = PartidoPolitico.objects.all()

        # Diccionario para almacenar los datos de votos por partido
        datos_grafica = {}

        # Llenar el diccionario con los datos de votos por partido
        for partido in partidos:
            votos = partido.votosporanio_set.all()
            if votos.exists():
                total_votos = sum(voto.cantidad_votos for voto in votos)
            else:
                total_votos = 0

            datos_grafica[partido.sigla] = total_votos

        print(partidos)
        print(datos_grafica)

        partidos = list(datos_grafica.keys())
        votes = list(datos_grafica.values())

        max_votes = np.max(votes)

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111)

        ax.pie(votes, labels=partidos)

        ax.set_title('Fake Polls')
        #ax.legend()

        plt.tight_layout()

        cwd = os.getcwd() #para la ruta del entorno

        # Guardar el gráfico como imagen
        plt.savefig(cwd + "\\fakeit\\static\\graphs\\votes.png")

        #print(graphic)
        #return graphic

if __name__ == "__main__":
    grafico.creargrafico()