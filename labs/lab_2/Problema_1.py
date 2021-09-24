import numpy as np

k = 2;

n = np.array([[5,3,8,10,2,1,5,1,0,2]]);

def sma(x,y):
    """
    Retorna un arreglo con valor de la media movil simple del 
    arreglo x con ventana y
    """
    size = x.shape;
    p = np.arange(y-1,size[1],1);
    m = np.arange(0,y,1);
    arrayfinal = np.zeros((1,size[1]-y+1))
    for i in p:
        c = 0;
        for e in m:
            c = c + x[0][i-e]
        arrayfinal[0][i-y+1] = c/y
    return arrayfinal[0]
        
print(sma(n,k))
    
    
    
    

    

