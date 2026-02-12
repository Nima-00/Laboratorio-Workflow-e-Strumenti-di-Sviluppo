"""Module Ex 5"""

import numpy as np


def fun_1(A: np.ndarray) -> np.ndarray:
    """Riga di somma massima"""
    idx = -1
    max_sum = -1
    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            s += A[i][j]
        if max_sum < s:
            max_sum = s
            idx = i
    return A[idx]


def fun_2(A: np.ndarray) -> np.ndarray:
    """Colonna di somma massima"""
    idx = -1
    max_sum = -1
    for j in range(A.shape[1]):
        s = 0
        for i in range(A.shape[0]):
            s += A[i][j]
        if max_sum < s:
            max_sum = s
            idx = j
    return A[:, idx]


def fun_3(A: np.ndarray) -> None:
    """Normalizza per righe"""
    C = np.zeros(A.shape)
    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            s += A[i][j]
        for j in range(A.shape[1]):
            C[i][j] = round(A[i][j] / s, 2)
    return C


def fun_4(A: np.ndarray) -> None:
    """Normalizza per colonne"""
    C = np.zeros(A.shape)
    for j in range(A.shape[1]):
        s = 0
        for i in range(A.shape[0]):
            s += A[i][j]
        for i in range(A.shape[0]):
            C[i][j] = round(A[i][j] / s, 2)
    return C


def fun_5(A: np.ndarray) -> None:
    """Normalizza la matrice"""
    C = np.zeros(A.shape)
    s = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            s += A[i][j]
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i][j] = round(A[i][j] / s, 2)
    return C
