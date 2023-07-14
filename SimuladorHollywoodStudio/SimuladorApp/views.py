from django.shortcuts import render
import pandas as pd
from .services.SimuladorService import Simulador
from .utils.graph import createGraph

# Create your views here.
def home(request):
    
    if request.method != ['POST']:
        monto = request.POST.get('monto')
        sim = Simulador()
        table_data = sim.simular()
        
    # Convierte la figura en un formato adecuado para la plantilla
    plot_div = createGraph()
    
    
    return render (request, 'home.html',{'plot_div': plot_div,
                                             'table_data': table_data})


