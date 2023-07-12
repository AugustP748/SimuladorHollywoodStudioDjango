from django.shortcuts import render
import plotly.graph_objects as go
from .services.SimuladorService import Simulador

# Create your views here.
def home(request):
    if request.method == ['POST']:
        monto = request.POST.get('monto')
        table_content = Simulador.simular()
        
        

        return render (request, 'home.html',{'plot_div': plot_div,'table_content': table_content})
    else:

        # Datos de la gráfica
        x = [float(i) for i in range(-10, 11)]
        y = [161 * i for i in x]

        # Crea la figura de Plotly
        fig = go.Figure(data=go.Scatter(x=x, y=y))
        fig.update_layout(
            autosize=False,
            width=400,
            height=250,
            margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=0
        ))
        # Convierte la figura en un formato adecuado para la plantilla
        plot_div = fig.to_html(full_html=False)
        return render (request, 'home.html',{'plot_div': plot_div})