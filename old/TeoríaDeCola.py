import pandas as pd

te_table = [(1, 1, 456,  45.6, 78.9),
            (1, 2, 785,  57.8, 33.7),
            (1, 3, 234,  22.1, 71.4),
            (2, 1, 984,  98.3, 83.2),
            (2, 2, 478,  67.8, 34.7),
            (2, 3, 593,  41.1, 56.9)]

# Convertir la lista en un DataFrame
df = pd.DataFrame(te_table)

# Renombrar las columnas
df = df.rename(columns={0: "dia", 1: "hora", 2: "visitantes", 3:"RR", 4:"MF"})


# Imprimir el DataFrame resultante
print(df)


registros_dia_2 = df.loc[df["dia"] == 2]
print(registros_dia_2)

# Calcular la media de la columna "RR"
media_rr = registros_dia_2["RR"].mean()

# Calcular la media de la columna "MF"
media_mf = registros_dia_2["MF"].mean()

# Calcular la suma de la columna "visitantes"
suma_visitantes = registros_dia_2["visitantes"].sum()

# Imprimir los resultados
print("Media de RR:", media_rr)
print("Media de MF:", media_mf)
print("Suma de visitantes:", suma_visitantes)

