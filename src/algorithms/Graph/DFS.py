

class Graph:
  
  def __init__(self, V):
    self.V = V  
    self.adj = [[] for i in range(V)] 
  
  def add(self, vertex, edge):
    self.adj[vertex].append(edge)
    self.adj[edge].append(vertex)
    
  def print(self):
    for i in range(len(self.adj)):
      for j in self.adj[i]:
        print(i, j)
        
  def dfs(self, vertex):
    visited = [False]*self.V
    st = [vertex]
    visited[vertex] = True
    while len(st) > 0:
      v = st.pop()
      for i in self.adj[v]:
        if not visited[i]:
          st.append(i)
          visited[i] = True
          print(i, end= " ")
    print("\n")
    
  def bfs(self, vertex):
    visited = [False]*self.V
    st = [vertex]
    visited[vertex] = True
    while len(st) > 0:
      v = st.pop(0)
      for i in self.adj[v]:
        if not visited[i]:
          st.append(i)
          visited[i] = True
          print(i, end= " ")
    print("\n")


g = Graph(5)
g.add(0,1)
g.add(1,2)
g.add(1,3)
g.add(2,4)
g.add(1,4)
g.add(3,4)
g.add(0,3)

for i in range(5): g.dfs(i)
print("bfs")
for i in range(5): g.bfs(i)