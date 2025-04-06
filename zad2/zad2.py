#Oliwia Dyszewska
#Zawsze mamy tablice, która przechowuje wszystkie liczby z zakresu od T[i] do T[i+p-1], sortujemy ją, a potem wstawiamy i usuwamy elementy tak zeby zawsze była posortowana i za każdym razem dodajemy k-ty element do koncowej sumy
from zad2testy import runtests

def ksum(T, k, p):
    def heapify(A, n, i):
        while True:
            mini = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and A[l] < A[mini]: #czy istnieje lewe dziecko i jego wartosc jest wieksza niz mini
                mini = l
            if r < n and A[r] < A[mini]: #czy istnieje prawe dziecko i jego wartosc jest wieksza niz mmini
                mini = r
            if mini == i:
                break
            A[i], A[mini] = A[mini], A[i]
            i = mini

    def heapsort(A):
        n = len(A)
        for i in range(n // 2, -1, -1): #budowanie kopca
            heapify(A, n, i)
        for i in range(n - 1, 0, -1): #sortowanie
            A[i], A[0] = A[0], A[i]
            heapify(A, i, 0)
    n = len(T)
    Z = T[:p] #tablica przechowujaca elementy z zakresu od 0 do p
    heapsort(Z)
    sum = Z[k-1]
    for i in range(1,n-p+1):
        Z.remove(T[i-1]) #usuniecie elementu z lewej strony
        new_index = i + p - 1 #znalezenie i dodanie nowego elementu
        new = T[new_index]
        j = 0
        while j < len(Z) and Z[j] >= new:
            j += 1
        Z.insert(j,new)
        sum += Z[k-1] #dodanie k-tego najwiekszego elementu z zakresu
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
