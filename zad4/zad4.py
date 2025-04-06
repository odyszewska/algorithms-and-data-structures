#Oliwia Dyszewska
#funkcja wykorzystuje dfs, zeby sprawdzic czy istnieje mozliwsoc przelotu z pkt x do y, uwzgledniajac pulap
from zad4testy import runtests

def Flight(L,x,y,t):
  def dfs(L, x, t, p, visited): #p - optymalny pułap przelotu
    visited[x] = True
    for v in L:
      if v[0] == x:
        if visited[v[1]] is False and abs(p - v[2]) <= t*2:
          p = v[2]
          dfs(L, v[1], t, p, visited)
  n = len(L)
  visited = [False]*n
  for v in L:
    if v[0] == x:
      p = v[2]
      dfs(L, v[1], t, p, visited)
  return visited[y]


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( Flight, all_tests = True )

L = input()
L = eval()
x = int(input())
y = int(input())
t = int(input())
print(Flight(L,x,y,t))
