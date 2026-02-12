"""Module Ex 4"""

import numpy as np


def fun_1(A: np.ndarray) -> int:
    """Restituisce il prodotto della somma delle diagonali"""
    d_1 = 0
    d_2 = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == j:
                d_1 += A[i][j]
            if i == (A.shape[1] - 1 - j):
                d_2 += A[i][j]
    return d_1 * d_2


def fun_2(A: np.ndarray, i: int, j: int):
    """Restituisce una matrice con due righe scambiate"""
    r_1 = 0
    r_2 = 1
    for i in range(A.shape[1]):
        t = A[r_1][i]
        A[r_1][i] = A[r_2][i]
        A[r_2][i] = t


def fun_3(A: np.ndarray, c_1: int, c_2: int):
    """Restituisce una matrice con due colonne scambiate"""
    for i in range(A.shape[1]):
        t = A[i][c_1]
        A[i][c_1] = A[i][c_2]
        A[i][c_2] = t


def fun_4(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Restituisce il prodotto matrice vettore"""
    c = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            c[i] += A[i][j] * b[j]
    return c


def fun_5(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Restituisce il prodotto di du matrici"""
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for z in range(A.shape[1]):
                C[i][j] += A[i][z] * B[z][j]
    return C
