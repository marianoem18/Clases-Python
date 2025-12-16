import streamlit as st
import pandas as pd

st.title("Hola, este es un curso de Python con Streamlit")

st.header("Productos disponibles")

st.sidebar.header("Carga de datos")
archivo = st.sidebar.file_uploader("Sube tu archivo JSON", type=["json"])

if archivo:
    df=pd.read_json(archivo)
    categoria = st.sidebar.selectbox("Selecciona una categoría", df['category'].unique())

    productos_filtrados = df[df['category'] == categoria]
    st.header(f"Productos en la categoría: {categoria}")
    st.dataframe(productos_filtrados)

else:
    st.write("Por favor, sube un archivo JSON para ver los productos.")    