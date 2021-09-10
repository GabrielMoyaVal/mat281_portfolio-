n = input("Ingrese el numero:")
m = int(n)

def collatz(x):
    
    """
        collatz(x)
        
        Determina si un par de numeros son amigos.
        
        Parameters
        ----------
        x: int
            Numero donde se inicia la serie.
            
        Returns
        ----------
        output: int
            Lista de enteros de la serie de Collatz.
    """
    
    lista = list()
    n = x
    while n != 1:
        lista.append(n);
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
    lista.append(1);
    return lista
list = collatz(m);
print(list);


