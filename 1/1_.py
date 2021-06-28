class Node:
    def __init__(self):
        self.next = None
        self.value = None

#sortowanie bąbelkowe - złożoność n^2

def bubble_sort(tab):
    n = len(tab)
    for i in range(n-1):  #n
        for j in range(n-1):  #n
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

#sortowanie przez wstawianie   - złożoność n^2


def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        key = tab[i]
        j = i - 1
        while i > -1 and tab[j]>tab[i]:
            tab[j+1] = tab[j]
            i = i - 1
        tab[i+1] = key

    return tab


#sortowanie przez wybieranie - sama napisałam 8)

def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[i]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

    return tab

a = [9,8,7,6]
print(insertion_sort(a))

#merge_sort


def insert_to_node(x, L):    #z wartownikiem (lista nigdy nie jest nonem)
    start = L   #wartownik
    while L.next != None and L.next.value < x.value:
        L = L.next

    x.next = L.next
    L.next = x

    return start


def print_list(L):
    if L is not None:
        print(L.value, end=" ")
        print_list(L.next)
    else:
        print()


L = Node()
node = Node()
node.value = 2
L.next = node
nn = Node()
nn.value = 5
node.next = nn
print_list(L)
a = Node()
a.value = 1
insert_to_node(a, L)
print_list(L)
b = Node()
b.value = 3
insert_to_node(b, L)
print_list(L)
c = Node()
c.value = 7
insert_to_node(c, L)
print_list(L)


def del_max(L):
    m = L.next
    m_prev = L
    prev = L
    L = L.next

    while prev.next != None:
        if prev.next.value > m.value:
            m_prev = prev
            m = prev.next
        prev = prev.next

    m_prev.next = m.next
    return L


del_max(L)
print_list(L)
del_max(L)
print_list(L)


#wyszukiwanie binarne
def bin_search(T, i, j, x):
    if(i > j):
            return None
    c = (i+j) // 2
    if(T[c] == x):
        ret = bin_search(T, i)
    if(T[c] > x):
        return bin_search(T, i, c, x)
    else:
        return bin_search(T, c, j, x)


T1 = [0, 1, 2, 3, 4]
print(bin_search(T1, 0, len(T1), 0))













