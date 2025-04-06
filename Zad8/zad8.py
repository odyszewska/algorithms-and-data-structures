#Oliwia Dyszewska
from zad8testy import runtests

def parking(X,Y):
    n = len(X)
    m = len(Y)
    odleglosci = [[float('inf')] * m for _ in range(n)]

    for j in range(m):
        odleglosci[0][j] = abs(X[0] - Y[j])
    for i in range(1, n):
        min_odl = float('inf')
        for j in range(i, m):
            min_odl = min(min_odl, odleglosci[i-1][j-1])
            odleglosci[i][j] = min_odl + abs(X[i] - Y[j])

    return min(odleglosci[n-1][n-1:m])

runtests( parking, all_tests = True )
