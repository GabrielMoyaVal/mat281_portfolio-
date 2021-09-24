import numpy as np

A = np.array([[4,9,2],[3,5,7],[8,1,6]])

def es_cuadrado_magico(A):
    """
    Devuelve True si la matriz A es magica, y falso si no lo es.
    """
    if A.shape[0] != A.shape[1]:
        print("La matriz no es cuadrada");
        return
    rec = np.arange(0,A.shape[0],1);
    marca = 0;
    c = 0;
    for i in rec:
        marca = marca + A[0][i];
    for x in np.arange(1,A.shape[0],1):
        c = 0;
        for y in np.arange(0,A.shape[0],1):
            c = c + A[x][y];
        if c != marca:
            return False
    for x in np.arange(0,A.shape[0],1):
        c = 0;
        for y in np.arange(0,A.shape[0],1):
            c = c + A[y][x];
        if c != marca:
            return False
    c = 0;
    for x in np.arange(0,A.shape[0],1):
        c = c + A[x][x];
    if c != marca:
        return False
    c = 0;
    m = int(A.shape[0])-1
    for x in np.arange(0,A.shape[0],1):
        c = c + A[m-x][x];
    if c != marca:
        return False
    return True

print(es_cuadrado_magico(A))
    

