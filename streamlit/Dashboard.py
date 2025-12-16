import streamlit as st
import pandas as pd
st.title("Dashboard de Productos")

st.sidebar.header("Carga de datos")
archivo = st.sidebar.file_uploader("Sube tu archivo JSON", type=["json"])

if archivo:
    df= pd.read_json(archivo)
    df['entry_date'] = pd.to_datetime(df['entry_date'])

    st.sidebar.header("Filtros")
    categorias = ["Todas"] + df['category'].unique().tolist()
    categoria = st.sidebar.selectbox("Selecciona una categoría", categorias)

    precio_min, precio_max = st.sidebar.slider(
        "Rango de precio",
        float(df['price'].min()),
        float(df['price'].max()),
        (float(df['price'].min()), float(df['price'].max())))
    
    df_filtrado = df.copy()

    if categoria != "Todas":
        df_filtrado = df_filtrado[df_filtrado['category'] == categoria]

    df_filtrado = df_filtrado[(df_filtrado['price'] >= precio_min) &
                              (df_filtrado['price'] <= precio_max)]    

    if df_filtrado.empty:
            st.write("No hay productos que coincidan con los filtros seleccionados.")
    else:
            col1, col2, col3 = st.columns(3)
            precio_promedio = df_filtrado['price'].mean()
            total_productos = len(df_filtrado) 
            valor_stock = (df_filtrado['price'] * df_filtrado['quantity']).sum()

            col1.metric("Precio Promedio", f"${precio_promedio:,.2f}")
            col2.metric("Total de Productos", total_productos)
            col3.metric("Valor Total de Stock", f"${valor_stock:,.2f}")
            
            st.subheader("Productos Filtrados")
            st.dataframe(df_filtrado)

            st.subheader("Distribucion de productos por categoria")
            conteo = df_filtrado.groupby("category")["name"].count()
            st.bar_chart(conteo)
else:    st.write("Por favor, sube un archivo JSON para ver los productos.")        