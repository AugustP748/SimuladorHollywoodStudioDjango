import pandas as pd

te_table = [(1, 1, 456, {"RR": 45.6, "MF": 78.9}),
            (1, 2, 785, {"RR": 57.8, "MF": 33.7}),
            (1, 3, 234, {"RR": 22.1, "MF": 71.4}),
            (2, 1, 984, {"RR": 98.3, "MF": 83.2}),
            (2, 2, 478, {"RR": 67.8, "MF": 34.7}),
            (2, 3, 593, {"RR": 41.1, "MF": 56.9})]

# Convertir la lista en un DataFrame
df = pd.DataFrame(te_table)

# Renombrar las columnas
df = df.rename(columns={0: "día", 1: "hora", 3: "atracciones", 2: "visitantes"})

# Establecer el índice
df = df.set_index(["día", "hora", "visitantes"])

# Imprimir el DataFrame resultante
print(df)

# Calcular la suma del contenido de cada diccionario dividido por "visitantes"
resultado = df.apply(lambda row: sum(row["atracciones"].values()) / row.name[2], axis=1)

# Renombrar la columna del resultado
resultado = resultado.rename("resultado")

# Agregar la columna al DataFrame principal
df["resultado"] = resultado

# Imprimir el DataFrame resultante
print(df)
