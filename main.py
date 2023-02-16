from lab import Graph

def leArquivoMatriz(arquivo):
    with open(arquivo, "r") as arquivo:
      linhas = arquivo.readlines()

    matriz = []

    for linha in linhas:
      linha = linha.rstrip("\n")
      elementos = list(linha)
      matriz.append(elementos)

    return matriz

graph = Graph()

leitura = input("Digite o arquivo: ")
matriz = leArquivoMatriz(leitura)
print(matriz)

graph.transformaMatrizGrafo(matriz)
print("\n")
print(graph.adjList)
print(graph.nodeCount)

