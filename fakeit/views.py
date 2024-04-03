from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
from django.views.generic import TemplateView
from . import creargrafico

# Create your views here.
class IndexView(generic.ListView):
    template_name = "graphic.html"
    context_object_name = "graph"

    partidos = ['PP', 'PSOE', 'Cs', 'UP', 'Vox', 'ERC', 'JxCat', 'PNV', 'EH Bildu', 'MP', 'PCE', 'IU']

    def post(self, request):
        parametroPartido = request.POST.get('paramPartido')
        parametroIncremento = request.POST.get('parametro_spinner')

        print(request.POST.get('paramPartido'))
        print("paco paco", parametroPartido, parametroIncremento)

        creargrafico.grafico.creargrafico()

        return render(self.request,  self.template_name,{'partidos': self.partidos})

    def get_queryset(self):
        print('paco paco paco1')
        return render(self.request,  self.template_name,{'partidos': self.partidos})
