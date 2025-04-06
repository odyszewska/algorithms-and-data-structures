#Oliwia Dyszewska
#Kod sortuje liste, uzywajac sortowania przez scalanie(merge sort). Dzieli liste na mniejsze fragmenty, a potem laczy je w posortowana liste.
from zad1testy import Node, runtests


def SortH(p,k):
    if p is None or p.next is None:
        return head

    def split(list, leng): #dzieli liste na 2 (1 o dlugosci leng), zwraca poczatek 2 listy
        i = 1
        while i < leng and list is not None:
            list = list.next
            i += 1
        if list is None:
            return None
        temp, list.next = list.next, None
        return temp

    def merge(list1, list2,list): #funkcja scalajaca 2 posortowane listy
        current = list
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        while current.next:
            current = current.next
        return current

    def length(list): #funkcja obliczajaca dlugosc listy
        leng = 0
        while list is not None:
            leng += 1
            list = list.next
        return leng

    len_p = length(p)
    list = Node()
    list.next = p
    dl = 1
    while dl < len_p:
        current = list.next
        tail = list
        while current:
            left = current
            right = split(left, dl)
            current = split(right, dl)
            tail = merge(left, right, tail)
        dl *= 2
    return list.next

runtests( SortH, all_tests = True )

