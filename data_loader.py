import pandas as pd
from config import conectar_supabase
import streamlit as st

@st.cache_data
def cargar_datos():
    try:
        supabase = conectar_supabase()
        response = supabase.table("credit_risk_data").select("*").execute()

        if not response.data:
            st.warning("⚠️ La tabla existe pero no contiene datos.")
            print("❌ Supabase retornó una respuesta vacía.")
            return pd.DataFrame()

        df = pd.DataFrame(response.data)
        print(f"✅ Datos cargados correctamente: {df.shape[0]} filas")
        return df

    except Exception as e:
        print(f"❌ Error al conectar con Supabase: {e}")
        st.error("No se pudo conectar a Supabase.")
        return pd.DataFrame()
