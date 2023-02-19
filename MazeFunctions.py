from graph import Graph
class MazeFunctions:

  def __init__(self, matriz) -> None:
    self.startNode, self.endNode = None, None
    self.graph = Graph(self.qtd_de_elementos(matriz))
    self.nodes = self.qtd_de_elementos(matriz)

  def exibeLabirinto(arquivo):
    with open(arquivo, "r") as arquivo:
      textoExibido = arquivo.read()
    print(textoExibido)

  def transformaMatrizGrafo(self, matriz):
    v = 1
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        if matriz[i][j] != '#' and matriz[i][j] != '█':
          if matriz[i][j] == 'S':
            self.startNode = v

          if matriz[i][j] == 'E':
            self.endNode = v

          if j < len(matriz[i])-1:
            if matriz[i][j+1] != '#' and matriz[i][j+1] != '█':
              self.graph.addUndirectedEdge(v, v+1)

          if matriz[i+1][j] != '#' and matriz[i+1][j] != '█':
            self.graph.addUndirectedEdge(v, v+len(matriz[1]))

        v += 1
    self.graph.adjList.pop(0)


  def qtd_de_elementos(self, matriz):
    qtd = 0
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        qtd += 1

    return qtd



  