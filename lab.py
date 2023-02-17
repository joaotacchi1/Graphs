class Graph:

  def __init__(self, nodeCount: int = 0, edgeCount: int =0, adjList: list[list[int]] = []) -> None:
    self.nodeCount = nodeCount
    self.edgeCount = edgeCount
    self.adjList = adjList
    self.startNode, self.endNode = None, None
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
    
  def addUndirectedEdge(self, u: int, v: int):
    self.addDirectedEdge(u,v)
    self.addDirectedEdge(v,u)

  def transformaMatrizGrafo(self, matriz):
    self.nodeCount = 0
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        if matriz[i][j] != "#" or matriz[i][j] != "█":
          if matriz[i][j] == "S":
            self.startNode = matriz[i][j]

          if matriz[i][j] == "E":
            self.endNode = matriz[i][j]

          if j < len(matriz):
            if matriz[i][j+1] != "#" or matriz[i][j+1] != "█":
              self.addUndirectedEdge(self.nodeCount, self.nodeCount + 1)

          if matriz[i+1][j] != "#" or matriz[i+1][j] != "█":
              self.addUndirectedEdge(self.nodeCount, self.nodeCount + 1)

        self.nodeCount += 1
 
    graph = Graph(self.nodeCount, self.edgeCount, self.adjList)
    return graph

  
  
  