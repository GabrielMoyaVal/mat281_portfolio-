n = input("Cantidad de Terminos de las sumatoria:");
m = int(n);

def factorial(y):
    """
    factorial(y)
    
    Calcula el factorial del numero y
    
    Parameters
    ----------
    y: int
        Numero al que se le aplica el factorial.
        
    Returns
    ----------
    output: int
        Factorial de y.
    """
    
    if y == 0 or y == 1:
        return 1;
    else:
        return (y*factorial(y-1));

def calculare (x):
    """
    calculare(x)
    
    Aproximacion de e usando el metodo de Euler con x terminos.
    
    Parameters
    ----------
    x: int
        Cantidad de terminos.
        
    Returns
    ----------
    output: float
        Aproximacion de e.
    """
    z = 0;
    if x == 0:
         return 0;
    else:
         for y in range(0,x):
             denominador = factorial(y);
             z += 1/denominador;
         return z;
e = calculare(m);
print("La aproximacion de e es:",e)