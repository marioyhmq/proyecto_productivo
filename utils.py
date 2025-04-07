import pandas as pd

def limpiar_datos(df):
    columnas = ["EDAD", "SALDO_TOTAL_TARJETA", "CUPO_PROMEDIO_TARJETA",
                "ANTIGUEDAD_TARJETA_ANIOS", "INSTRUCCION", "MORA"]
    for col in columnas:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df.dropna()
