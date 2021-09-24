import pandas as pd
import os

df = pd.read_csv(os.path.join("data","ocupation.csv"),sep=",")
df.head()

print("1) La cantidad de observaciones del data frame es", df.shape[1]);

print("\n2) La cantidad de columnas son ", df.shape[1]);

print("\n3) Se tienen las siguientes columnas");

col = df.columns;
for i in range(0,col.shape[0],1):
    print(df.columns[i]);
    
print("\n4) El indice es el siguiente");
print(df.index);

print("\n5)Se presenta cada columna con su tipo de dato");
print(df.dtypes);

print("\n6) A continuacion se presenta los datos estadisticos:");
print(df.describe());

print("\n7) Columna ocupation:");
for i in df["ocupation"]:
    print(i);

print("\n8) La cantidad de ocupaciones son:");
cont = 0;
for i in df["ocupation"].unique():
    cont += 1;
print(cont)

print("\n9) La ocupacion que mas se repite es:")
cont = 0;
ocupacion = str()
for i in df["ocupation"].unique():
    aux = 0;
    for e in df["ocupation"]:
        if i == e:
            aux += 1;
    if aux > cont:
        cont = aux;
        ocupacion = i;
print(ocupacion)
print("La cantidad de veces que se repite es:")
print(cont)

print("\n10) La edad media de los usuarios es:")
print(df["age"].mean());
    
"""
No pude conseguirme la base de datos por lo que no conosco bien 
los nombres de las columnas. intente adivinar como se llamaban
"""
    

    

