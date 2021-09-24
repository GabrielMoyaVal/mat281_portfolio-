import numpy as np

a = np.array([[1,2,3,4,5,6,7,8,9,10]])

def strides(a,n,p):
    
    """
    Devuelve la matriz generada con el arreglo a, con n columnas
    """
    matriz = np.zeros((n,n));
    reca = np.arange(0,n,1);
    if a.shape[1] < n+(n-1)*p:
        print("El arreglo es muy corto");
        return 
    for i in reca:
        matriz[0][i] = a[0][i];
    rec = np.arange(1,n,1);
    c = 0;
    for e in rec:
        c += p;
        for i in reca:
            matriz[e][i] = a[0][c+i];
    return matriz

print(strides(a,4,2))