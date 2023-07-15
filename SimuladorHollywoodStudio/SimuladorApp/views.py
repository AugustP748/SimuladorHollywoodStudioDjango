from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from .services.SimuladorService import Simulador
from .utils.graph import createGraph

# Create your views here.
def home(request):
    # Convierte la figura en un formato adecuado para la plantilla
    plot_div = createGraph()
    return render (request, 'home.html',{'plot_div': plot_div})

def get_table_data(request):
    sim = Simulador()
    table_data = sim.simular()
    if(len(table_data) > 0):
        data = {'message':"Successfully",'table_data':table_data}
    else:
        data = {'message':"Not Found"}
        
    return JsonResponse(data,safe=False)
