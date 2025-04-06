#Oliwia Dyszewska
#Algorytm oblicza sumy prefiksowe, by potem dzięki nim obliczyc sile dla kazdego punktu
from zad3testy import runtests

def dominance(P):
  n = len(P)

  #liczymy sumy prefiksowe licznikow wspolrzednych x i y
  prefiks_x = [0] * (n + 1)
  prefiks_y = [0] * (n + 1)
  for p in P:
    x, y = p
    prefiks_x[x] += 1
    prefiks_y[y] += 1
  for i in range(1, n + 1):
    prefiks_x[i] += prefiks_x[i - 1]
    prefiks_y[i] += prefiks_y[i - 1]

  #sprawdzamy sile kazdego punktu
  maks = 0
  for p in P:
    x, y = p
    strenght = prefiks_x[x - 1] + prefiks_y[y - 1] - n + 1
    maks = max(maks, strenght)

  return maks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
