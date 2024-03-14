import sys
sys.path.append('src')
sys.path.append('models')
sys.path.append('data')
from librerias import *
from utils import *

st.set_page_config(layout="wide")

def generar_grafico(dataframe, tipo_grafico, variables):
    tipos_graficos = {
        "histogram": px.histogram,
        "scatter": px.scatter,
        "line": px.line,  # Diagrama de línea de tiempo
        "pie": px.pie,  # Diagrama de pie
        "bar": px.bar,  # Gráfico de barras con líneas
        "heat map": px.imshow,  # Mapa de calor
        "area": px.area,  # Gráfico de área
        'Box': px.box
    }
    
    if tipo_grafico in tipos_graficos:
        fig = tipos_graficos[tipo_grafico](dataframe, x=variables[0], y=variables[1] if len(variables) > 1 else None)
        return fig
    else: raise ValueError("Tipo de gráfico no válido")
st.title( 'Resumen de la Data')

# Cargar Dataframes
if ['dataframes','Nombres_Especificos','column_descriptions'] not in st.session_state:
    st.session_state.dataframes,st.session_state.nombres_especificos,st.session_state.column_descriptions = load_dataframes()
dataframes = st.session_state.dataframes
Nombres_Especificos = st.session_state.nombres_especificos
column_descriptions   = st.session_state.column_descriptions

# Seleccionar dataframe

df_name = st.selectbox('Seleccione un dataframe', list(dataframes.keys()))
df = dataframes[df_name]
column_order = ['Periodo de Cobertura', 'Ano de Cobertura', 'Year', 'Month', 'Sexo', 'Cotizante', 'Tipo_de_ARS']

create_data =  {x: "multiselect"  for x in df.columns if x in column_order or df[x].dtype == 'object'}

st.header(df_name)
ignorelist =['Periodo de Cobertura']
ignorelist = [x for x in ignorelist if x in df.columns]

tab3, tab4 = st.sidebar.tabs(["DataFrame Filter", "Graph Filter"])
st.session_state.all_widgets = create_widgets(df,create_data, ignore_columns=ignorelist,container=tab3)#,sideContainer=sideContainer  )  

res = filter_df(df, st.session_state.all_widgets)

tab1, tab2 = st.tabs(["Original DataFrame", "Result DataFrame"])
if st.checkbox("Mostrar dataframe"):
    # Mostrar resumen del dataframe
    
    tab1.dataframe(df)
    tab2.dataframe(res) 
     

# Mostrar nombres de las columnas y su descripción
if st.checkbox("Mostrar descripción de las columnas"):
    

    if df_name in column_descriptions:
        st.write('Descripción de las columnas:')
        st.write(column_descriptions[df_name])
        st.write(df.describe())
    else:
        st.write('No se encontraron descripciones para las columnas de este DataFrame.')


column_order = ['Periodo de Cobertura', 'Ano de Cobertura', 'Year', 'Month', 'Sexo', 'Cotizante', 'Tipo_de_ARS']
columnas_categoricas = [x for x in ['Tipo_de_ARS','Cotizante','Sexo'] if x in df.columns]
columnas_tiempo = [x for x in ['Periodo de Cobertura', 'Ano de Cobertura', 'Year', 'Month'] if x in df.columns]
# Crear widget para la selección de columna categórica para los gráficos de pie


