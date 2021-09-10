n = input("Cantidad de Terminos de las sumatoria:");
m = int(n);

def calcularpi (x):
    """
    calcularpi(x)
    
    Aproximacion de pi usando el metodo de Leibniz con x terminos.
    
    Parameters
    ----------
    x: int
        Cantidad de terminos.
        
    Returns
    ----------
    output: float
        Aproximacion de pi
    """
    z = 0;
    if x == 0:
         return 0;
    else:
         for y in range(1,x+1):
             numerador = (-1)**(y+1);
             denominador = 2*y-1;
             z += numerador/denominador;
         z = z*4
         return z;
pi = calcularpi(m);
print ("La aproximacion de pi es:",pi)
    
    

    

