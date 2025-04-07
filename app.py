import streamlit as st
import pandas as pd
from data_loader import cargar_datos
from utils import limpiar_datos
from model import entrenar_modelo, evaluar_modelo
from dashboard import graficos_basicos

# Título
st.title("📊 Reporte Crediticio + ML con Streamlit")
st.markdown("✅ Datos cargados desde Supabase:")

# Cargar datos
df = cargar_datos()

if df is None or df.empty:
    st.error("⚠️ No se encontraron datos disponibles desde Supabase.")
    st.stop()

# Limpiar datos
df = limpiar_datos(df)

# Mostrar una vista previa
st.dataframe(df.head())

# Visualización básica
graficos_basicos(df)

# Entrenamiento de modelo
modelo, X_test, y_test = entrenar_modelo(df)

# Evaluación del modelo
st.subheader("📈 Evaluación del Modelo")
evaluacion = evaluar_modelo(modelo, X_test, y_test)
st.text(evaluacion)

# Formulario de predicción
st.sidebar.header("🔍 Predicción para Cliente Nuevo")
edad = st.sidebar.slider("Edad", 18, 75)
saldo = st.sidebar.number_input("Saldo total tarjeta", value=1000.0)
cupo = st.sidebar.number_input("Cupo promedio", value=2000.0)
antiguedad = st.sidebar.slider("Antigüedad (años)", 0, 20)
instruccion = st.sidebar.selectbox("Nivel de instrucción", options=[1, 2, 3, 4, 5])

# Mostrar entrada simulada
st.sidebar.markdown("### Datos del cliente")
st.sidebar.write({
    "Edad": edad,
    "Saldo": saldo,
    "Cupo": cupo,
    "Antigüedad": antiguedad,
    "Instrucción": instruccion
})

# Simulación básica de predicción
st.sidebar.markdown("### Resultado de la predicción:")
st.sidebar.success("✅ Aprobado (Simulado)")
