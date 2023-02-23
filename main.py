from MazeFunctions import *
import time

arquivo = ''
while arquivo != '0':

    arquivo = input("Digite o nome do arquivo ou 0 para sair:"+"\n"+"Exemplo: toy"+"\n>>")
    if arquivo != '0':
        arquivo = "maze/"+arquivo+".txt"
    else:
        print("Encerrando...")
        break
    mazeGraph = MazeFunctions(arquivo)
    mazeGraph.transformaMatrizGrafo()
    start = time.time()
    print("Vizualização do labirinto:")
    mazeGraph.exibeLabirinto(arquivo)
    print(">>>>>>>>>Dados do labirinto<<<<<<<<<")
    print("Início: ", mazeGraph.startNode)
    print("Fim: ", mazeGraph.endNode)
    print("Trajeto entre os nós: ", busca_saida(mazeGraph.graph, mazeGraph.startNode, mazeGraph.endNode))
    print("Coordenadas na matriz: ", mazeGraph.coordenadas())
    print("Tempo de execução em segundos:", time.time()-start)
