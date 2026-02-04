"""Module Ex 1"""

import numpy as np


def fun_1(A: np.ndarray) -> None:
    """Funzone stampa matrice"""
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            print(A[i][j], end="\t")
        print()


def fun_2(A: np.ndarray) -> int:
    """Somma una matrice"""
    s = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            s = s + A[i][j]
    return s


def fun_3(A: np.ndarray) -> int:
    """Ritorna il minimo di una matrice"""
    m = A[0][0]

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] < m:
                m = A[i][j]
    return m


def fun_4(A: np.ndarray) -> None:
    """Stampa diagonale di una matrice"""
    for i in range(A.shape[0]):
        print(A[i][i])


def fun_5(A: np.ndarray) -> None:
    """Somma le righe di una matrice"""
    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            s += A[i][j]
        print(s)
