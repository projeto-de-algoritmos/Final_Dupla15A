from django.shortcuts import render, HttpResponseRedirect
from .forms import Formulario, Formulario2
from TrabalhoFinal.functions.menu import menu


def home(request):
    return render(request, 'home.html', {})


def index(request):
    
    if request.method == 'POST':

        form = Formulario(request.POST or None)


        if form.is_valid():

            inicio = form['partida'].value()
            final = form['destino'].value()
            autonomia = form['autonomia'].value()
           
            status = menu(0,inicio,final,autonomia)
            if(status == -1):
                return HttpResponseRedirect('error/')
            else:
                return HttpResponseRedirect('path/')
               
    else:
        form = Formulario()

    args = {}
    return render(request, 'menor_caminho.html', {'form': form})

def path_result(request):
    return render(request, 'mapa.html', {})

def error(request):
    return render(request, 'error.html', {})

def index2(request):
    
    if request.method == 'POST':

        form = Formulario2(request.POST or None)

        if form.is_valid():

            inicio = form['partida'].value()
            final = form['destino'].value()
            paradas = form['paradas'].value()
 
            try:
                paradas.append(final)
                menu(1,inicio,paradas,'')
                return HttpResponseRedirect('path/')
            
            except :
                return HttpResponseRedirect('error/')
            

    else:
        form = Formulario2()
   
    return render(request, 'menor_caminho2.html', {'form': form})