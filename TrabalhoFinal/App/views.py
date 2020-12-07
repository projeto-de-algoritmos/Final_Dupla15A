from django.shortcuts import render, HttpResponseRedirect
from .forms import Formulario, Formulario2
from TrabalhoFinal.functions.menu import menu


def home(request):
    return render(request, 'home.html', {})


def index(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Formulario(request.POST or None)
        # check whether it's valid:

        if form.is_valid():
            # print(cidades)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            inicio = form['partida'].value()
            final = form['destino'].value()
            autonomia = form['autonomia'].value()
            print(form['partida'].value())
            print(form['destino'].value())
            print(form['autonomia'].value())
            try:
                menu(0,inicio,final,autonomia)
                return HttpResponseRedirect('path/')
            
            except :
                return HttpResponseRedirect('error/')
            
            
            

    # if a GET (or any other method) we'll create a blank form 
    else:
        form = Formulario()

    # return render(request, 'name.html', {'form': form})
    return render(request, 'menor_caminho.html', {'form': form})

def path_result(request):
    return render(request, 'mapa.html', {})

def error(request):
    return render(request, 'error.html', {})

def index2(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Formulario2(request.POST or None)
        # check whether it's valid:

        if form.is_valid():
            # print(cidades)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            inicio = form['partida'].value()
            final = form['destino'].value()
            paradas = form['paradas'].value()
            # autonomia = form['paradas'].value()
            print(form['partida'].value())
            print(form['destino'].value())
            print(form['paradas'].value())

            try:
                paradas.append(final)
                menu(1,inicio,paradas,'')
                return HttpResponseRedirect('path/')
            
            except :
                return HttpResponseRedirect('error/')
            

    else:
        form = Formulario2()

    # return render(request, 'name.html', {'form': form})
    return render(request, 'menor_caminho.html', {'form': form})