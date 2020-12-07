import sys
import time
from TrabalhoFinal.functions.funcoes import  busca_caminho, cidades, prim,busca_caminho_dijkstra, imagem_mapa
from TrabalhoFinal.functions.Graph import Grafo


edges = [   ('Cuiaba - MT', 'Goiania - GO', 895), 
            
            ('Cuiaba - MT', 'Posto - MT/GO', 400), 
            
            ('Posto - MT/GO', 'Goiania - GO', 495), 

# ------------------------------------------------------

            ('Cuiaba - MT', 'Campo Grande - MS', 707),
            
            ('Cuiaba - MT', 'Posto - MT/MS', 505), 
            
            ('Posto - MT/MS', 'Campo Grande - MS', 202), 

# ------------------------------------------------------

            ('Goiania - GO', 'Campo Grande - MS', 846), 
            
            ('Goiania - GO', 'Posto - GO/MS', 350), 
            
            ('Posto - GO/MS', 'Campo Grande - MS', 496), 

# ------------------------------------------------------

            ('Goiania - GO', 'Belo Horizonte - MG', 890),
            
            ('Goiania - GO', 'Posto - GO/MG', 500), 
            
            ('Posto - GO/MG', 'Belo Horizonte - MG', 390), 
# ------------------------------------------------------

            ('Campo Grande - MS', 'Sao Paulo - SP', 1013), 
            
            ('Campo Grande - MS', 'Posto - MS/SP', 490), 
            
            ('Posto - MS/SP', 'Sao Paulo - SP', 523), 

# ------------------------------------------------------

            ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
            
            ('Sao Paulo - SP', 'Posto - SP/RJ', 220), 
            
            ('Posto - SP/RJ', 'Rio de Janeiro - RJ', 221), 

# ------------------------------------------------------

            ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 
            
            ('Sao Paulo - SP', 'Posto - SP/MG', 281), 
            
            ('Posto - SP/MG', 'Belo Horizonte - MG', 311), 

# ------------------------------------------------------

            ('Belo Horizonte - MG', 'Vitoria - ES', 523), 
            
            ('Belo Horizonte - MG', 'Posto - MG/ES', 213), 
            
            ('Posto - MG/ES', 'Vitoria - ES', 310), 

# ------------------------------------------------------

            ('Rio de Janeiro - RJ', 'Vitoria - ES', 527),
            
            ('Rio de Janeiro - RJ', 'Posto - RJ/ES', 275), 
            
            ('Posto - RJ/ES', 'Vitoria - ES', 252)]

edges2 = [   ('Cuiaba - MT', 'Goiania - GO', 895), 
            ('Cuiaba - MT', 'Campo Grande - MS', 707),

            ('Goiania - GO', 'Campo Grande - MS', 846), 
            ('Goiania - GO', 'Belo Horizonte - MG', 890), 

            ('Campo Grande - MS', 'Sao Paulo - SP', 1013), 

            ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
            ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 

            ('Belo Horizonte - MG', 'Vitoria - ES', 523), 

            ('Rio de Janeiro - RJ', 'Vitoria - ES', 527)]


def menu(op,inicio,final,arg3):
 
    if(op == 0):
        mapa = edges
        cidades(mapa)
        status = busca_caminho(inicio,[final],mapa, int(arg3))
        if(status == -1):
            return -1

    else:
        mapa = edges2
        cidades(mapa)
        busca_caminho_dijkstra(inicio,final,mapa)
    
    return 0

    # print("\tAté mais....")