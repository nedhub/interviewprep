from collections import defaultdict



class Graph:
    def __init__(self,vertives):
        self.graph = defaultdict(list)
        self.V = vertives


    def addEdge(self,u,v):
        self.graph[u].append(v)

    def neighbor_gen(self,v):
        for k in self.graph[v]:
            yield k


    def nonRecursiveTopologicslSortUtil(self, v, vistied, stack):


        working_stack = [(v,self.neighbor_gen(v))]

        while len(working_stack) > 0:

            v, gen = working_stack[-1]
            vistied[v] = True

            working_stack.pop()

            continue_flag = True
            while continue_flag: 
                next_neighbor = next(gen,None)


                if next_neighbor is None:
                    continue_flag = False


                    stack.append(v)
                    continue


                if not(vistied[next_neighbor]):
                    working_stack.append((v,gen))
                    working_stack.append((next_neighbor,self.neighbor_gen(next_neighbor)))
                    continue_flag = False



    def nonRecursiveTopologicalSort(self):

        visited = [False]*self.V

        stack = []

        for i in range(self.V):
            if not(visited[i]):
                self.nonRecursiveTopologicslSortUtil(i, visited,stack)

        print(stack[::-1])


    
g = Graph(6)
g.addEdge(5,2);
g.addEdge(5,0);
g.addEdge(4,0);
g.addEdge(4,1);
g.addEdge(2,3);
g.addEdge(3,1);

print("The following is a Toplogical Sort of the given graph")

g.nonRecursiveTopologicalSort()



