from sys import maxsize
import heapq

class graph():
    def __init__(self):
        self.qtdV = 0
        self.V = dict()
    def print_graph(self):
        print("Impressao de grafos:")
        for i in self.V:
            for vizinho, w in self.V[i].items():
                print(i,"-(", w, ")-", vizinho,sep="")

    def add_vertice(self, v): 
        if v not in self.V:
            self.V[v] = {}

    def add_edge(self, v1, v2, w=1):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.V:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.V:
            print("Vertex ", v2, " does not exist.")
        else:
    # estamos levando em conta um grafo bidirecional
            self.V[v1][v2] = w
            self.V[v2][v1] = w
            self.qtdV+=1

    def get_NroVertices(self):
        return self.qtdV

    def get_Vertices(self):
        return self.V.keys()

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.V}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.V[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

    def shortest_path(self, initial_vert, final_vert):
        paths = self.dijkstra(final_vert)
        if final_vert not in paths:
            print("not found")
        else :
            return paths[initial_vert]

    def change_weight(self,v1,v2):
        pass