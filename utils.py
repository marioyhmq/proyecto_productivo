import pandas as pd

def limpiar_datos(df):
    columnas_objetivo = [
        "EDAD",
        "SALDO_TOTAL_TARJETA",
        "CUPO_PROMEDIO_TARJETA",
        "ANTIGUEDAD_TARJETA_ANIOS",
        "INSTRUCCION",
        "MORA"
    ]

    # Solo convertir columnas si existen
    columnas_validas = [col for col in columnas_objetivo if col in df.columns]

    for col in columnas_validas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Advertencia en consola si faltan columnas
    columnas_faltantes = list(set(columnas_objetivo) - set(columnas_validas))
    if columnas_faltantes:
        print("❗ Columnas faltantes no procesadas:", columnas_faltantes)

    return df.dropna(subset=columnas_validas)
