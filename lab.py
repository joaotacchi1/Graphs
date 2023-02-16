class Graph:

  def __init__(self, nodeCount: int = 0, edgeCount: int =0, adjList: list[list[int]] = []) -> None:
    self.nodeCount = nodeCount
    self.edgeCount = edgeCount
    self.adjList = adjList
    if adjList == []:
      for _ in range(self.nodeCount):
        self.adjList.append([])

  def exibeLabirinto(arquivo):
    with open(arquivo, "r") as arquivo:
      textoExibido = arquivo.read()
    print(textoExibido)

  def addDirectedEdge(self, u: int, v: int):
    if u >= self.nodeCount or v >= self.nodeCount or u < 0 or v < 0:
      print(f"Edge ({u},{v}) could not be added because one of this value is out of the allowed range (0,{self.nodeCount},-1)")
      return

  def transformaMatrizGrafo(self, matriz):
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        self.nodeCount += 1
        if matriz[i][j] != "#" and matriz[i][j] != None:   
          if i < len(matriz) - 1 and matriz[i+1][j] not in self.adjList:
            self.adjList.append(matriz[i+1][j])
            self.addDirectedEdge(i,j)

          if j < len(matriz[i]) - 1 and matriz[i][j+1] not in self.adjList:
            self.adjList.append(matriz[i][j+1])
            self.addDirectedEdge(i,j)

    graph = Graph(self.nodeCount, self.edgeCount, self.adjList)
    return graph


  
  
  