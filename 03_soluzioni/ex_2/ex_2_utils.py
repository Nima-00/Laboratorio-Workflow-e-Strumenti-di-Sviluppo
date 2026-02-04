"""Module Ex 2"""

import numpy as np


def fun_1(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Somma due matrici"""
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i][j] = A[i][j] + B[i][j]
    return C


def fun_2(A: np.ndarray) -> int:
    """Conta il numero di elementi uguali a due"""
    n = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] == 2:
                n += 1
    return n


def fun_3(A: np.ndarray) -> int:
    """Conta gli elementi divisibili per tre"""
    s = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] % 3 == 0:
                s += 1
    return s


def fun_4(A: np.ndarray) -> list:
    """List zeros' positions"""
    pos = []
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] == 0:
                pos.append((i, j))
    return pos


def fun_5(A: np.ndarray) -> np.ndarray:
    """Restituisce la matrice trasposta"""
    C = np.zeros((A.shape[1], A.shape[0]))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[j][i] = A[i][j]
    return C
