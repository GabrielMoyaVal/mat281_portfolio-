n_1 = input("Primer Numero:");
m_1 = int(n_1);
n_2 = input("Segundo Numero:");
m_2 = int(n_2);

def amigos(x,y):
    
    """
    amigos(x,y)
    
    Determina si un par de numeros son amigos.
    
    Parameters
    ----------
    x: int
        Numero que se determina si es amigo del otro.
        
    y: int
        Numero que se determina si es amigo del otro.
    Returns
    ----------
    output: boolean
        Booleano que determina si el par de numeros son amigos.
    """
    
    sigma_x = 0;
    sigma_y = 0;
    for x_1 in range(1,x):
        if x % x_1 == 0:
            sigma_x += x_1;
    for y_1 in range(1,y):
        if y % y_1 == 0:
            sigma_y += y_1;
    if sigma_x == y and sigma_y == x:
        return True
    else:
        return False
    
pos = amigos(m_1,m_2);
print(pos)
