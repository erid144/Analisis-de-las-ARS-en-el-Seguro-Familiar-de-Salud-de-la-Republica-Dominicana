import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar la tabla
@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Seleccionar la tabla
selected_table = st.sidebar.selectbox("Selecciona una tabla:", Tablas)

# Mostrar los primeros registros de la tabla
df = load_data(selected_table)
st.write("Primeros registros de la tabla:")
st.write(df.head())

# Realizar exploración de datos utilizando Plotly
st.write("Exploración de datos:")
# Por ejemplo, crear un histograma interactivo con Plotly
columna_numerica = st.selectbox("Selecciona una columna numérica:", df.select_dtypes(include=['int', 'float']).columns)
fig = px.histogram(df, x=columna_numerica, title=f"Histograma de {columna_numerica}")
st.plotly_chart(fig)