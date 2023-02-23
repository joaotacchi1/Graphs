class Graph:
  def __init__(self, countNodes: int= 0, countEdges: int = 0, adjList: list[list[int]] = []) -> None:
    self.countNodes = countNodes
    self.countEdges = countEdges
    self.adjList = adjList
    if adjList == []:
      for _ in range(self.countNodes):
        adjList.append([])
  
  def addDirectedEdge(self, u: int, v: int):
    if u >= self.countNodes or v >= self.countNodes or u < 0 or v < 0:
      print(f"Edge ({u},{v}) could not be added because one of this value is out of the allowed range (0, {self.countNodes},-1)")
      return
    
    self.adjList[u].append(v)
    self.countEdges += 1

  def addUndirectedEdge(self, u: int, v: int):
    self.addDirectedEdge(u, v)
    self.addDirectedEdge(v, u)


