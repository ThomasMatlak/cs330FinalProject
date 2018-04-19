class Graph:

    def __init__(self, vertex, src = 0):
        self.v = vertex
        self.graph = []
        self.src = src # src node

    def isSrc(self, src):
        self.src = src

    def addEdge(self, u, v):
        # undirected graph
        self.graph.append([u, v])
        self.graph.append([v, u])

    def printGraph(self, distance):
        # print the solution
        for i in range(self.v):
            print("Distance from node", i, "to source", self.src,": ", distance[i])


def BellmanFord(graph):
    infi = float("Inf")
    distance = [infi] * graph.v
    distance[graph.src] = 0

    for i in range((graph.v-1)*2):
        for u, v in graph.graph:
            if distance[u] != infi and distance[u] + 1 < distance[v]:
                distance[v] = distance[u] + 1

    graph.printGraph(distance)

G = Graph(5, 2)
G.addEdge(0, 2)
G.addEdge(0, 3)
BellmanFord(G)
G.addEdge(1, 2)
G.isSrc(1)
BellmanFord(G)


# def DistanceVector(graph):
#     distance = float(["Inf"]) * graph.v
#     distance[graph.src] = 0
#     for x in graph.vertex:

