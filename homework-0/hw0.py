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
        color = [0] * (self.size+1)
        queue = []

        # insert node 1
        color[1] = 1
        queue.append(int(1))

        # BFS walk
        while queue:
            u = queue.pop()

            for v in self.adjacencyList[u]:
                if color[v] == color[u]:
                    return False
                elif color[v] == 0:
                    if color[u] == 1:
                        color[v] = 2
                    else:
                        color[v] = 1
                    queue.append(v)

        return True

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
