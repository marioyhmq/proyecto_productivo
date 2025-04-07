import streamlit as st
from data_loader import cargar_datos
from utils import limpiar_datos
from model import entrenar_modelo, evaluar_modelo
from dashboard import graficos_basicos
import pandas as pd

# Cargar datos
df = cargar_datos()

if df.empty:
    st.error("⚠️ No se encontraron datos en Supabase.")
    st.stop()

df = limpiar_datos(df)

# Título
st.title("📊 Reporte Crediticio + ML con Streamlit")
st.write("✅ Datos cargados desde Supabase:")
st.dataframe(df.head())

# Visualización
graficos_basicos(df)

# Entrenamiento de modelo
modelo, X_test, y_test = entrenar_modelo(df)

# Evaluación
st.subheader("📈 Evaluación del Modelo")
st.text(evaluar_modelo(modelo, X_test, y_test))

# Formulario de predicción
st.sidebar.header("🔍 Predicción para Cliente Nuevo")
edad = st.sidebar.slider("Edad", 18, 75)
saldo = st.sidebar.number_input("Saldo total tarjeta", value=1000.0)
cupo = st.sidebar.number_input("Cupo promedio", value=2000.0)
antiguedad = st.sidebar.slider("Antigüedad (años)", 0, 20)
instruccion = st.sidebar.selectbox

