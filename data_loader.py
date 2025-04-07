import pandas as pd
from config import conectar_supabase
import streamlit as st

@st.cache_data
def cargar_datos():
    supabase = conectar_supabase()
    response = supabase.table("credit_risk_data").select("*").execute()
    return pd.DataFrame(response.data)
