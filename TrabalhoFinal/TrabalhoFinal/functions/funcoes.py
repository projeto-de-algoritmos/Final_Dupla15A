from queue import PriorityQueue
from math import inf
from graphviz import Digraph
from TrabalhoFinal.functions.Graph import Grafo
import time



def criar_mapa():
    qtd_cidade = 0
    while(qtd_cidade <= 0):
        qtd_cidade = int(input("Quantidade de cidades: " ))
    
    mapa = []

    for i in range(qtd_cidade):
        nome_cidade = input("Nome da cidade: " )
        qtd_vizinhos = 0
        while(qtd_vizinhos <= 0):
            qtd_vizinhos = int(input("Numero de cidades vizinhas: " ))

        for j in range(qtd_vizinhos):
            nome_vizinho, distancia = input("Nome da cidade(vizinha) e a distancia: ").split()
            mapa.append((nome_cidade, nome_vizinho, distancia))

    return mapa

def dijkstra(graph, raiz):
    fila = PriorityQueue()  
    caminho = {}  
    for v in graph.vertices():
        if v == raiz:
            caminho[v] = [[], 0]  
        else:
            caminho[v] = [[], inf]  

        fila.put((caminho[v][1], v))  

    vertices_restantes = list(graph.vertices()) 

    for i in range(len(graph.vertices())):
        u = fila.get()[1]  
        vertices_restantes.remove(u) 

        for v in vertices_restantes:  
            du = caminho[u][1] 
            w = graph.custo(u, v) 
            dv = caminho[v][1]  
            if du + w < dv:  
                caminho[v][1] = du + w  
                caminho[v][0] = caminho[u][0] + [u]  
                fila.queue.remove((dv, v)) 
                fila.put((caminho[v][1], v))

    print("Caminho: ", caminho)
    return caminho

def bellman(graph, raiz, tanque):
    
    fila = PriorityQueue()  
    caminho = {}  
    autonomia = {}
    semCombustivel = {}

    for v in graph.vertices():
        if v == raiz:
            # Distancia raiz é igual a zero
            caminho[v] = [[], 0]
            autonomia[v] = tanque  
  
        else:
            # Todas as demais distancias são infinito
            caminho[v] = [[], inf]  
            autonomia[v] = tanque 


        fila.put((caminho[v][1], v))  

    for i in range(len(graph.vertices())):
        u = fila.get()[1]  

        for v in list(graph.vertices()):  
            du = caminho[u][1] 
            w = graph.custo(u, v) 
            dv = caminho[v][1]  

            if autonomia[u] >= w:

                if du + w < dv:  

                    caminho[v][1] = du + w  
                    caminho[v][0] = caminho[u][0] + [u]  
                    fila.queue.remove((dv, v)) 
                    fila.put((caminho[v][1], v))
                    autonomia[v] = autonomia[u] - w
                    autonomia[v] = tanque
    
            else:

                print("FICOU SEM COMBUSTIVEL, A AUTONOMIA DO SEU VEICULO É INCOPATIVEL PARA ESSE TIPO DE VIAGEM.")
                
                if du + w < dv:  

                    caminho[v][1] = 999999 
                    caminho[v][0] = caminho[u][0] + [u]  
                    fila.queue.remove((dv, v)) 
                    fila.put((caminho[v][1], v))
                    autonomia[v] = autonomia[u] - w
                    autonomia[v] = 0

    for v in list(graph.vertices()):  
        
        du = caminho[u][1] 
        w = graph.custo(u, v) 
        dv = caminho[v][1]  
        if du + w < dv:  
            # Contem ciclos negativos.
            return -1

    return caminho

def imagem_mapa(e, opcao,listCaminho,distanciaTotal,nome_mapa):
    mapa = Digraph(nome_mapa, filename=nome_mapa, node_attr={'color': 'lightblue2'}, engine='sfdp')
    mapa.attr(size='80', shape='ellipse', fontsize='20', rankdir='LR')
    mapa.attr('node', shape='doublecircle')

    for i in e:
        mapa.edge(i[0], i[1], label=str(i[2]), color='black', constraint='false',dir='none')

    if(opcao !=0):
        print("----------")
        print(listCaminho)
        for v in range(0, len(listCaminho) - 1):
            if v == len(listCaminho) - 2:
                mapa.edge(listCaminho[v], listCaminho[v + 1], label=str(distanciaTotal), color='red', constraint='true')
            else:
                mapa.edge(listCaminho[v], listCaminho[v + 1], color='red', constraint='false')
        
    mapa.format = 'svg'
    mapa.render()
    
    print("Mapa está sendo gerado aguarde...")
    time.sleep(3)
    
def busca_caminho(partida, parada, mapa, tanque):

    g = Grafo({})
    for e in mapa:
        g.adiciona_arestas(*e)
    
    distanciaTotal = 0
    visitados = []
    caminhoPercorrido = []
    for i in parada:
    
        distance = bellman(g, partida, tanque)

        print("Distancia: ", distance)

        if int(distance[i][1]) >= 999999:

            visitados = [str(partida)]
            caminhoPercorrido.append(visitados)
            distanciaTotal = "FICOU SEM COMBUSTIVEL, A AUTONOMIA DO SEU VEICULO É INCOPATIVEL PARA ESSE TIPO DE VIAGEM."

        else:
            visitados.append(partida)
            partida = i
            caminhoPercorrido.append(distance[i][0])
            distanciaTotal += int(distance[i][1])
    
    visitados.append(partida)
    caminhoPercorrido.append(parada[-1:])

    for g in caminhoPercorrido:
            print("\n caminhoPercorrido lista macro: ", g)

    listCaminho = []
    for g in caminhoPercorrido:
        for h in g:   
            listCaminho.append(h)
            print("\n caminhoPercorrido lista: ", h)
    
    print(listCaminho)

    if listCaminho.count(partida) >= 2:
        print("ERROR")
        return -1

    imagem_mapa(mapa,1,listCaminho,distanciaTotal,"./App/static/img/mapa_resultado")
    return 0
    
def cidades(mapa):
    print("Cidades Cadastradas ")
    a = []
    for i in mapa:
        if(not(i[0] in a)):
            a.append(i[0])
        if(not(i[1] in a)):
            a.append(i[1])
    print(a)

def prim(graph, raiz):
    vertice = [raiz]  
    arestas_selecionadas = []  

    peso = 0  

    vertices_remanescentes = list(graph.vertices())  
    vertices_remanescentes.remove(raiz)  

    for i in range(len(vertices_remanescentes)):  
        custo_minimo = inf  
        va, vb = None, None  
        for v1 in vertice:  
            for v2 in vertices_remanescentes:  
                custo = graph.custo(v1, v2)  
                if custo < custo_minimo:  
                    va = v1
                    vb = v2
                    custo_minimo = custo

        if custo_minimo < inf:  
            arestas_selecionadas.append((va, vb, custo_minimo))  
            vertice.append(vb)  
            vertices_remanescentes.remove(vb)  
            peso += custo_minimo
    
    a = []
    for i in arestas_selecionadas:
        if(not(i[0] in a)):
            a.append(i[0])
        if(not(i[1] in a)):
            a.append(i[1])
    
    caminho = a 
    
    return caminho, peso

def busca_caminho_dijkstra(partida, parada, mapa):
    g = Grafo({})
    for e in mapa:
        g.adiciona_arestas(*e)
    
    distanciaTotal = 0
    visitados = []
    caminhoPercorrido = []
    for i in parada:
        distance = dijkstra(g, partida)
        visitados.append(partida)
        partida = i
        caminhoPercorrido.append(distance[i][0])
        distanciaTotal += int(distance[i][1])
    
    visitados.append(partida)
    caminhoPercorrido.append(parada[-1:])
    listCaminho = []

    for g in caminhoPercorrido:
        for h in g:
            listCaminho.append(h)
    
    print(listCaminho)

    imagem_mapa(mapa,1,listCaminho,distanciaTotal,"./App/static/img/mapa_resultado")
