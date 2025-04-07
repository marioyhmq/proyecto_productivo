import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def graficos_basicos(df):
    st.subheader("Distribución de Mora")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x="MORA", ax=ax1)
    st.pyplot(fig1)

    st.subheader("Saldo Total vs Edad")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="EDAD", y="SALDO_TOTAL_TARJETA", hue="MORA", ax=ax2)
    st.pyplot(fig2)
