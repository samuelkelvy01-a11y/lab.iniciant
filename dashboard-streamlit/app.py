import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Vendas", layout="centered")

st.title("Dashboard de Vendas")

@st.cache_data
def load_data(path="vendas.csv"):
    df = pd.read_csv(path)
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0)
    df["Total"] = df["Quantidade"] * df["Valor"]
    return df

df = load_data()

faturamento = df["Total"].sum()
qtd_total = df["Quantidade"].sum()

st.metric("Faturamento", f"R$ {faturamento:,.2f}")
st.metric("Quantidade total", int(qtd_total))

st.subheader("Faturamento por produto")
st.bar_chart(data=df.set_index("Produto")["Total"]) 

st.subheader("Dados")
st.dataframe(df)
