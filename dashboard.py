import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def graficos_basicos(df):
    df.columns = df.columns.str.strip().str.upper()

    if df.empty:
        st.warning("⚠️ El DataFrame está vacío. No se puede graficar.")
        return

    if "MORA" not in df.columns:
        st.error("❌ La columna 'MORA' no está disponible para graficar.")
        st.write("Columnas disponibles:", df.columns.tolist())
        return

    fig, ax1 = plt.subplots()
    sns.countplot(data=df, x="MORA", ax=ax1)
    st.pyplot(fig)
