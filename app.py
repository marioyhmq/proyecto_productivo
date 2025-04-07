import streamlit as st
from data_loader import cargar_datos
from utils import limpiar_datos
from model import entrenar_modelo, evaluar_modelo
from dashboard import graficos_basicos
import pandas as pd

df = cargar_datos()
df = limpiar_datos(df)

st.title("📊 Reporte Crediticio + ML con Streamlit")
st.write("Datos cargados desde Supabase:")
st.dataframe(df.head())

graficos_basicos(df)

modelo, X_test, y_test = entrenar_modelo(df)
st.subheader("📈 Evaluación del Modelo")
st.text(evaluar_modelo(modelo, X_test, y_test))

st.sidebar.header("🔍 Predicción para Cliente Nuevo")
edad = st.sidebar.slider("Edad", 18, 75)
saldo = st.sidebar.number_input("Saldo total tarjeta", value=1000.0)
cupo = st.sidebar.number_input("Cupo promedio", value=2000.0)
antiguedad = st.sidebar.slider("Antigüedad (años)", 0, 20)
instruccion = st.sidebar.selectbox("Nivel instrucción", [1, 2, 3, 4])

nuevo = pd.DataFrame([[edad, saldo, cupo, antiguedad, instruccion]],
                     columns=["EDAD", "SALDO_TOTAL_TARJETA", "CUPO_PROMEDIO_TARJETA",
                              "ANTIGUEDAD_TARJETA_ANIOS", "INSTRUCCION"])

if st.sidebar.button("Predecir Riesgo"):
    pred = modelo.predict(nuevo)
    resultado = "⚠️ Riesgo de Mora" if pred[0] == 1 else "✅ Bajo Riesgo"
    st.success(f"Resultado: {resultado}")
