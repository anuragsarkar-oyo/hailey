

class Graph:
  
  def __init__(self, vertex):
    self.vertex = vertex
    self.adj = [[] for i in range(vertex)] 
    
  def add(self, vertex, edge):
    self.adj[vertex].append(edge)
    
    
  def findPath(self, start):
    visited = [False]*self.vertex
    visited[start] = True
    st= [start]
    count = 1
    while len(st)>0:
      print(st)
      point = st.pop(0)
      visited[point] = True
      for i in self.adj[point]:
        if not visited[i]:
          st.append(i)
          visited[i] = True
          count += 1
        print(i)
    return count
      
      
a = [5,4,0,3,1,6,2]
vertex = len(a)
g = Graph(vertex)
for i,x in enumerate(a):
  g.add(i, x)

print(g.findPath(0))