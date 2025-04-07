import pandas as pd

def limpiar_datos(df):
    # Limpiamos los nombres de las columnas para evitar errores invisibles
    df.columns = df.columns.str.strip().str.upper()

    # Lista de columnas clave (ahora en mayúsculas, para hacer match real)
    columnas_objetivo = [
        "EDAD",
        "SALDO_TOTAL_TARJETA",
        "CUPO_PROMEDIO_TARJETA",
        "ANTIGUEDAD_TARJETA_ANIOS",
        "INSTRUCCION",
        "MORA"
    ]

    # Verificamos qué columnas existen realmente
    columnas_validas = [col for col in columnas_objetivo if col in df.columns]

    if not columnas_validas:
        print("❌ Ninguna de las columnas objetivo está presente.")
        return df  # Devuelve sin modificar

    # Convertimos columnas a numéricas solo si están presentes
    for col in columnas_validas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Advertencia en consola si faltan columnas
    columnas_faltantes = list(set(columnas_objetivo) - set(columnas_validas))
    if columnas_faltantes:
        print("⚠️ Columnas no encontradas en el DataFrame:", columnas_faltantes)

    # Eliminamos filas con valores faltantes solo en las columnas relevantes
    return df.dropna(subset=columnas_validas)
