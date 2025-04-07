import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def graficos_basicos(df):
    if df.empty:
        st.warning("⚠️ No hay datos disponibles para mostrar gráficos.")
        return

    st.subheader("Distribución de Mora")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="MORA", ax=ax)
    st.pyplot(fig)
