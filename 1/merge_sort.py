from random import randint, seed
from math import inf
#Merge Sort z Cormena

def merge(A, p, q, r):
    # ilosc scalanych elementow
    n1 = q - p + 1
    n2 = r - q

    L = [0 for _ in range(n1 + 1)]
    R = [0 for _ in range(n2 + 1)]

    # przypisywanie odpowiednich polowek do dwoch tablic
    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]

    # dodanie na koncu wartownika, ktory sprawia, ze nie trzeba sprawdzac, czy listy sa juz puste
    L[n1] = inf
    R[n2] = inf

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, p, r):
    if p < r:  # indeks poczatkowy < indeks koncowy
        q = (p + r) // 2  # srodek
        mergeSort(A, p, q)  # sortuje tablice T[p, q] (lewa czesc)
        mergeSort(A, q + 1, r)  # sortuje tablice T[q+1, r] (prawa czesc)
        merge(A, p, q, r)  # scalenie w dobrej kolejnosci

    return A


def mergesort(T):
    n = len(T) - 1
    T = mergeSort(T, 0, n)
    return T


seed(42)

n = 10
T = [randint(1, 11) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
