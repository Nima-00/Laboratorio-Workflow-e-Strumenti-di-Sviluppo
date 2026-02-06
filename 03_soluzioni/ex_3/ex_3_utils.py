"""Module Ex 3"""

import numpy as np


def fun_1(A: np.ndarray) -> bool:
    """Controlla se una matrice è diagonale"""
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i != j and A[i][j] != A[j][i]:
                return False
    return True


def fun_2(A: np.ndarray) -> bool:
    """Controlla se una matrice è simmetrica"""
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] != A[j][i]:
                return False

    return True


def fun_3(A: np.ndarray) -> bool:
    """Controlla se una matrice è triangolare inferiore"""
    for i in range(A.shape[0]):
        for j in range(i + 1, A.shape[1]):
            if A[i][j] != 0:
                return False
    return True


def fun_4(A: np.ndarray, r: int, c: int) -> int:
    """Somma meno una riga e una colonna"""
    s = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i != r and j != c:
                s = s + A[i][j]
    return s


def fun_5(A: np.ndarray, r: int, c: int) -> np.ndarray:
    """Rimuovi una riga e una colonna"""
    B = np.zeros((A.shape[0] - 1, A.shape[1] - 1))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i < r and j < c:
                B[i][j] = A[i][j]
            elif i < r and j > c:
                B[i][j - 1] = A[i][j]
            elif i > r and j < c:
                B[i - 1][j] = A[i][j]
            elif i > r and j > c:
                B[i - 1][j - 1] = A[i][j]
    return B
