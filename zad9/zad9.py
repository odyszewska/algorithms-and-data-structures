#Oliwia Dyszewska
from zad9testy import runtests

def trip(M):
    m = len(M)
    n = len(M[0])
    kierunki = [(1,0), (-1,0), (0,1), (0,-1)] #gora, dol, prawo, lewo
    tab = [[-1 for _ in range(n)] for _ in range(m)]

    def dfs(x, y):
        if tab[x][y] != -1:
            return tab[x][y]
        max_dl = 1

        for kierunek in kierunki:
            nx = x + kierunek[0]
            ny = y + kierunek[1]
            if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[x][y]:
                max_dl = max(max_dl, 1 + dfs(nx, ny))
        tab[x][y] = max_dl
        return max_dl

    wynik = 0
    for i in range(m):
        for j in range(n):
            wynik = max(wynik, dfs(i, j))
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
