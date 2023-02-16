class Graph:
  def __init__(self, countNodes: int = 0, countEdges: int = 0, adjList: list[list[int]] = []) -> None:
    #self.nodes = [(0, 0, "#"), (0, 1, " "), (0, 2), ...]
    self.countNodes = countNodes
    self.countEdges = countEdges
    self.adjList = adjList
    if adjList == []:
      for _ in range(self.countNodes):
        adjList.append([])
  
  def addDirectedEdge(self, u: int, v: int):
    if u >= self.countNodes or v >= self.countNodes or u < 0 or v < 0:
      print(f"Edge ({u},{v}) could not be added because one of this value is out of the allowed range (0,{self.countNodes},-1)")
      return
    
    self.adjList[u].append(v)
    self.countEdges += 1

  def addUndirectedEdge(self, u: int, v: int):
    self.addDirectedEdge(u,v)
    self.addDirectedEdge(v,u)

  def addNode(self):
    self.adjList.append([])
    self.countNodes += 1

  def degreeOut(self, u:int) -> int:
    return len(self.adjList[u])

  def degreeIn(self, u: int) -> int:
    count = 0
    for i in range(len(self.adjList)):
    #   if u in self.adjList[i]:
    #     count += 1
    # return count
      for j in range(len(self.adjList[i])):
        if u == self.adjList[i][j]:
          count += 1
    return count

  def highestDegreeOut(self) -> int:
    node = 0
    maxDegreeOut = 0

    for i in range(self.countNodes):
      if self.degreeOut(i) > maxDegreeOut:
        maxDegreeOut = self.degreeOut(i)
        node = i
    return node

  def density(self):
    return self.countEdges / (self.countNodes * (self.countNodes - 1))

  def complete(self):
    #return self.density() == 1
    #return self.countEdges == self.countNodes * (self.countNodes - 1)
    for u in range(len(self.adjList)):
      if len(self.adjList[u]) != self.countNodes - 1:
        return False
    return True    

  def regular(self):
    degree = len(self.adjList[0])
    for i in range(1, len(self.adjList)):
      if len(self.adjList[i]) != degree:
        return False
    return True   

  def complement(self):
    complementGraph = Graph(self.countNodes, adjList=[])
    for i in range(len(self.adjList)):
      for j in range(self.countNodes):
        if j not in self.adjList[i] and j != i:
          complementGraph.addDirectedEdge(i,j)
    return complementGraph

  def __str__(self):
    repr = ""
    for adj in self.adjList:
        repr += str(adj) + "\n"
    return repr 

  def buscaLargura(self, s):
    desc = []
    for u in range(self.countNodes):
      desc.append(0)
    #desc = [0 for i in range(len(self.adjList))]
    q = [s]
    r = [s]
    desc[s] = 1

    while len(q) != 0:
      u = q.pop(0)
      for v in self.adjList[u]:
        if desc[v] == 0:
          q.append(v)
          r.append(v)
          desc[v] = 1
    return r

  def connected(self):
    if len(self.buscaLargura(5)) != self.countNodes:
      return False
    return True   

  def buscaProfundidade(self, s):
    desc = [0 for i in range(len(self.adjList))]
    S = [s]
    R = [s]
    desc[s] = 1

    while len(S) != 0:
      u = S[-1]
      desempilha = self.auxBuscaProfundidade(u,desc)
      if desempilha != -1:
        S.append(desempilha)
        R.append(desempilha)
        desc[desempilha] = 1
      else:
        S.pop()  
    return R

  def BuscaProfundidadeAux(self, u, desc):
    for v in self.adjList[u]:
      if desc[v] == 0:
        return v
    return -1
  
  def buscaProfundidadeRecursiva(self, s):
    desc = [0 for _ in range (self.countNodes)]
    R = []
    self.buscaProfundidadeAuxRec(s, desc, R)
    return R

  def buscaProfundidadeAuxRec(self, u, desc, R):
    desc[u] = 1
    R.append(u)

    for v in self.adjList[u]:
      if desc[v] == 0:
        self.buscaProfundidadeAuxRec(v, desc, R)
