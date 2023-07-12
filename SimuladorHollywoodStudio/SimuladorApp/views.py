from django.shortcuts import render

from .services.SimuladorService import Simulador

# Create your views here.
def home(request):
    if request.method == ['POST']:
        monto = request.POST.get('monto')
        table_content = Simulador.simular()
        print(table_content)
    return render(request,'home.html')