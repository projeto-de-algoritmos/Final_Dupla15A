import sys
import time
from funcoes import criar_mapa, imagem_mapa, busca_caminho, cidades, prim
from Graph import Grafo


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

            # ('Cuiaba - MT', 'Campo Grande - MS', 707),

            # ('Goiania - GO', 'Campo Grande - MS', 846), 
            # ('Goiania - GO', 'Belo Horizonte - MG', 890), 

            # ('Campo Grande - MS', 'Sao Paulo - SP', 1013), 

            # ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
            # ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 

            # ('Belo Horizonte - MG', 'Vitoria - ES', 523), 

            # ('Rio de Janeiro - RJ', 'Vitoria - ES', 527)]

def menu():
    print("Bem-Vindo")
    print("O programa tem o objetivo de encontrar caminhos em um mapa.")
    print("Mapa: ")
    print("1 - Para usar o mapa padrão")
    print("2 - Criar meu mapa")
    print("3 - Sair ")
    opcao = 0
    
    while(opcao <=0):
        
        opcao = int(input("Digite a opção: "))

        if(opcao == 1 ):
            imagem_mapa(edges,0,[],0,"mapa")
            mapa = edges
        
        elif (opcao == 2):
            mapa = criar_mapa()
            imagem_mapa(mapa,0,[],0,"mapa")
            
        elif (opcao == 3):
            print("Saindo...")
            # sys.exit()
        else:
            print("Opcao não invalida....")
            opcao = 0
    
    print('\n' * 100)
    print("--------------------------------------")
    print("Opcoes:")
    print("1- Buscar menor caminho até outra cidade")
    print("2- Buscar caminho passando por pontos")
    print("3- Buscar menor caminho para todos os pontos")
    opcao = 0
    while(opcao<=0 ):
        opcao = int(input("Digite: "))
        print('\n' * 100)

        # menor caminho entre entre duas cidades(dijkstra)
        if(opcao == 1):
            cidades(mapa)
            
            inicio = input("Ponto de partida(cidade): ")
            
            final = input("Ponto final(cidade): ")

            tanque = input("Qual a autonomia do seu veiculo? Automia media é 600. \n")

            busca_caminho(inicio,[final],mapa, int(tanque))

        # passando por determinados pontos
        # elif (opcao == 2):
        #     cidades(mapa)
        #     entrada = input("Ponto de partida(cidade): ")
        #     c = int(input("Por quantos pontos deseja passar antes do final? "))
        #     final = input("Ponto final(cidade): ")
        #     paradas = []
        
        #     for i in range(c):
        #         cont = i+1
        #         parada = input("%d° Ponto(cidade): "%cont)
        #         paradas.append(parada)
        #     paradas.append(final)

        #     busca_caminho(entrada,paradas,mapa)

        elif(opcao == 3):
            cidades(mapa)
            entrada = input("Ponto inicial(cidade): ")
            g = Grafo({})
            for e in mapa:
                g.adiciona_arestas(*e)

            pontos, distancia_total = prim(g, entrada)  # Retorna as arestas e o peso
            imagem_mapa(mapa,1,pontos,distancia_total,"mapa_resultado")
           
        else:
            opcao = 0

    print("\tAté mais....")

menu()