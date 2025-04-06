#Oliwia Dyszewska
#Do E dodajemy mozliwe przeloty utowrzone z pkt z S ustawiajac ich czas na 0, potem szukamy najkrotszej trasy uzywajac BFS
from zad5testy import runtests
from collections import deque
def spacetravel( n, E, S, a, b ): #n - ilosc planet, E - mozliwe przeloty, S - osobliwosci, a - startowa, b - docelowa
    # Dodanie możliwych przelotów między planetami leżącymi przy osobliwościach
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            u = S[i]
            v = S[j]
            if i != j and [v,u,0] not in E:
                E.append((u, v, 0)) #Czas podróży ustawiamy na 0

    time = [float('inf')] * n # Tablica czasów podróży między planetami
    time[a] = 0  # Czas podróży z planety a do niej samej

    #BFS
    queue = deque([a])
    while queue:
        current_planet = queue.popleft()
        for u, v, t in E:
            if u == current_planet and time[v] > time[u] + t:
                time[v] = time[u] + t
                queue.append(v)
            elif v == current_planet and time[u] > time[v] + t:
                time[u] = time[v] + t
                queue.append(u)

    if time[b] == float('inf'): # Jeśli nie istnieje trasa z planety a do planety b
        return None
    return time[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )