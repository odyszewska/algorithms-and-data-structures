#Oliwia Dyszewska
from zad6testy import runtests

from collections import deque
def jumper( G, s, w ):
    n = len(G)

    # Tworzymy graf skoków
    jump_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                jump_graph[u].append((v, G[u][v]))

    # Funkcja pomocnicza do wyznaczania maksimum z wag krawędzi na ścieżce
    def max_weight_on_path(path):
        max_weight = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            max_weight = max(max_weight, G[u][v])
        return max_weight

    # Algorytm Dijkstry z modyfikacją wag krawędzi
    dist = [float('inf')] * n
    dist[s] = 0
    visited = [False] * n
    while True:
        unvisited = [(dist[v], v) for v in range(n) if not visited[v]]
        if not unvisited:
            break
        u = min(unvisited)[1]
        if u == w:
            break
        visited[u] = True
        for v, w in jump_graph[u]:
            new_dist = dist[u] + max(w, max_weight_on_path([s, u, v]))
            if new_dist < dist[v]:
                dist[v] = new_dist
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                new_dist = dist[u] + G[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    return dist[w]


runtests( jumper, all_tests = True )