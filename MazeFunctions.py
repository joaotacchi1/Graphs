from graph import Graph
class MazeFunctions:

  def __init__(self, arquivo) -> None:
    self.matriz = self.leArquivoMatriz(arquivo)
    self.startNode, self.endNode = None, None
    self.coordinates: list[tuple[int, int]] = []
    self.graph = Graph(self.qtd_de_elementos(self.matriz),0,[])


  def leArquivoMatriz(self, arquivo):
    with open(arquivo, "r") as arquivo:
      linhas = arquivo.readlines()

    matriz = []

    for linha in linhas:
      linha = linha.rstrip("\n")
      elementos = list(linha)
      matriz.append(elementos)

    return matriz

  def exibeLabirinto(self,arquivo):
    with open(arquivo, "r") as arquivo:
      textoExibido = arquivo.read()
    print(textoExibido)


  def transformaMatrizGrafo(self):
    no = 0
    i=0
    j=0
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        if self.matriz[i][j] != '#':
          if self.matriz[i][j] == 'S':
            self.startNode = no


          if self.matriz[i][j] == 'E':
            self.endNode = no

          if j < len(self.matriz[i])-1:
            if self.matriz[i][j+1] != '#':
              self.graph.addUndirectedEdge(no, no+1)

          if self.matriz[i+1][j] != '#':
            self.graph.addUndirectedEdge(no, no+len(self.matriz[1]))

        no += 1

  def qtd_de_elementos(self, matriz):
    qtd = 0
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        qtd += 1
        self.coordinates.append([i, j])

    return qtd

  def coordenadas(self, xy = []):
    trajeto_de_saida = busca_saida(self.graph, self.startNode, self.endNode)
    while trajeto_de_saida != []:
      xy.append(self.coordinates[trajeto_de_saida[0]])
      trajeto_de_saida.pop(0)
    return xy

def busca_saida(graph, s, e, desc = None):
  if desc is None:
    desc = set()
  desc.add(s)
  if s == e:
    return [s]
  for adj in graph.adjList[s]:
    if adj not in desc:
      caminho = busca_saida(graph, adj, e, desc)
      if caminho is not None:
        return [s] + caminho
  return None





  
