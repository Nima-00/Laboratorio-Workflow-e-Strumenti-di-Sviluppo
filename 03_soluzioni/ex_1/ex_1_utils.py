"""Module Ex 1"""


def stampa_matrice(A: list[list]) -> None:
    """Funzone stampa matrice"""
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="\t")
        print()


def somma_matrice(A: list[list]) -> int:
    """Somma una matrice"""
    s = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            s = s + A[i][j]
    return s


def min_matrice(A: list[list]) -> int:
    """Ritorna il minimo di una matrice"""
    m = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < m:
                m = A[i][j]
    return m


def diag_matrice(A: list[list]) -> None:
    """Stampa diagonale di una matrice"""
    for i in range(len(A)):
        print(A[i][i])


def somma_righe(A: list[list]) -> None:
    """Somma le righe di una matrice"""
    for i in range(len(A)):
        s = 0
        for j in range(len(A[i])):
            s += A[i][j]
        print(s)
