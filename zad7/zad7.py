#Oliwia Dyszewska
from zad7testy import runtests
from collections import deque

def maze( L ):
    n = len(L)
    if L[0][0] == '#' or L[n-1][n-1] == '#':
        return -1

    # Kierunki ruchu: Dół, Prawo, Góra
    directions = [(1, 0), (0, 1), (-1, 0)]

    # Kolejka do BFS
    queue = deque([(0, 0, 0)])  # (x, y, liczba_odwiedzonych_komnat)

    # Tablica do zapamiętywania maksymalnej liczby odwiedzin dla każdej komnaty
    memo = [[-1] * n for _ in range(n)]
    memo[0][0] = 0

    max_rooms = -1

    while queue:
        x, y, count = queue.popleft()

        # Jeśli dotarliśmy do końcowej komnaty (n-1, n-1), aktualizujemy max_rooms
        if (x, y) == (n-1, n-1):
            max_rooms = max(max_rooms, count)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and L[nx][ny] == '.' and memo[nx][ny] < count + 1:
                memo[nx][ny] = count + 1
                queue.append((nx, ny, count + 1))

    return max_rooms if max_rooms != -1 else -1


runtests( maze, all_tests = True )
