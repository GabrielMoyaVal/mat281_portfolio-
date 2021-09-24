import pandas as pd
import os

df = pd.read_csv(os.path.join("data","Automobile.csv")).set_index('index')
df.head()

"""
1) Se borran los NULL
"""
mask = lambda df: df.notnull().all(axis=1);
df = df[mask];
df.head;
print(df);

print("\2) La compañia mas cara es:")
df_temp = df.sort_values(ascending = False,"Price");
df_temp = df_temp.head(1);
print(df_temp["Company"]);

print("\n3) La informacio de la Comañia Toyota Cars es:");
df_temp = df.loc[df["Company"] == "Toyota Cars"];
print(df_temp.describe());

print("\n4) La cantidad de coches por compañia son:")
for i in df["Company"].unique():
    aux = 0;
    for e in df["Company"]:
        if i == e:
            aux += 1;
    print(i,aux);
    
print("\n5) El coche mas caro por compañia es:")
for i in df["Company"].unique():
    df_temp = df.loc[df["Company"] == i];
    df_temp = df_temp.sort_values(ascending = False,"Price");
    df_temp = df_temp.head(1);
    print(df_temp["Company"],df_temp["Price"]);

    



