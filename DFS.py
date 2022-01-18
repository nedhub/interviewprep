# Python3 program to print DFS traversal
# from a given graph from collections import defaultdict

#This class represents a directded graph using adjacency list representation


from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFSUtil(self, v, visited):


        visited.add(v)
        print(v, end=" ")



        for neighour in self.graph[v]:
            if neighour not in visited:
                self.DFSUtil(neighour, visited)


    def DFS(self, v):


        visted = set()


        self.DFSUtil(v, visted)



g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)



g.DFS(2)

