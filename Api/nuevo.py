import requests
import pandas as pd
import streamlit as st

@st.cache_data(ttl=600)
def obtener_datos_api():
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()  # Verifica si hubo un error HTTP
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener datos de la API: {e}")
        return pd.DataFrame()
        

df = obtener_datos_api()

if not df.empty:
    st.title("Productos de Fake Store API, estadisticas principales")
    average_price = df['price'].mean()
    total_products = len(df)
    col1, col2 = st.columns(2)
    col1.metric("Precio Promedio", f"${average_price:.2f}")
    col2.metric("Total de Productos", total_products)

    st.subheader("Filtros")
    categorias = st.multiselect("Selecciona Categorías", df['category'].unique(), default=df['category'].unique()) 
    min_price, max_price = st.slider("Rango de Precios", float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())))

    st.header("Productos Filtrados")
    filtered_df = df[(df['category'].isin(categorias) & (df['price'] >= min_price) & (df['price'] <= max_price))]
    st.dataframe(filtered_df)

    st.header("Visualización de Precio promedio por Categoría")
    price_by_category = filtered_df.groupby('category')['price'].mean().reset_index()
    st.bar_chart(price_by_category, x='category', y='price')

else:
    st.warning("No se pudieron cargar los datos de la API.")
