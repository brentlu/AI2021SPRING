import sys

class Graph:

    def __init__(self, n):
        self.size = n
        self.adjacencyList = [[] for i in range(n+1)]

    def setEdge(self, u, v):
        self.adjacencyList[u].append(v)
    
    def bipartite(self):
        """Check if this graph is bipartite

        Returns:
          True/False
        """
        #TODO
        pass


if __name__=="__main__":

    with open(sys.argv[1]) as f:

        lines = f.readlines()
        size = int(lines[0])
        graph = Graph(size)

        for i in range(1, graph.size+1):
            neighbors = [int(v) for v in lines[i].split()]
            for v in neighbors:
                graph.setEdge(i, v)

    print(graph.bipartite())
