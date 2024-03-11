
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Mi Título Personalizado")

# Ahora puedes agregar el resto de tu código de Streamlit
st.title("Bienvenido a mi aplicación de Streamlit")

def load_dataframes():
  """
  Carga todos los Dataframes en una sesión de Streamlit y devuelve un diccionario con los nombres y Dataframes.

  Parámetros:
    Ninguno.

  Retorno:
    Diccionario con los nombres y Dataframes.
  """
  # Lista de archivos
  Tablas = [
    'data/Base_Creada/Afiliados_Edad_Sexo_Cotizacion.csv',
    'data/Base_Creada/RC_Tabla_Regiones.csv',
    'data/Base_Creada/RC_Datos_Regionales_Cotizacion.csv',
    'data/Base_Creada/RC_Region_Salud_Total.csv',
    'data/Base_Creada/RC_Region_Geografica_Total_Combinado.csv',
    'data/Base_Creada/SFS_Regimen_Sexo_Porcentaje_Tasa.csv',
    'data/Base_Creada/Financiamiento_Dispersado_TipoARS_postMes.csv',
    'data/Base_Creada/Financiamiento_Dispersado_Salario.csv',
    'data/Base_Creada/FinanciamientoARS_SaludPIB_Regimen.csv',
    'data/Base_Creada/PrestacionesPBS.csv',
    'data/Base_Creada/Ingresos_Gastos_Siniestralidad.csv',
    'data/Base_Creada/Ingresos_Gastos_Siniestralidad_Anual.csv'
  ]

  # Lista de nombres específicos
  Nombres_Especificos = [
    'Afiliados Edad Sexo Cotizacion',
    'Tabla Regiones',
    'Datos Regionales Cotizacion',
    'Region Salud Total',
    'Region Geografica Total Combinado',
    'SFS Regimen Sexo Porcentaje Tasa',
    'Financiamiento Dispersado TipoARS postMes',
    'Financiamiento Dispersado Salario',
    'FinanciamientoARS SaludPIB Regimen',
    'PrestacionesPBS',
    'Ingresos Gastos Siniestralidad',
    'Ingresos Gastos Siniestralidad Anual'
  ]

  # Diccionario para almacenar Dataframes
  dataframes = {}

  # Cargar Dataframes
  for i in range(len(Tablas)):
    dataframes[Nombres_Especificos[i]] = pd.read_csv(Tablas[i])
  # Guardar Dataframes y nombres específicos en Session State
  st.session_state.dataframes = dataframes
  st.session_state.nombres_especificos = Nombres_Especificos
  return dataframes

def generar_grafico(dataframe, tipo_grafico, variables):
    if tipo_grafico in tipos_graficos:
        fig = tipos_graficos[tipo_grafico](dataframe, x=variables[0], y=variables[1] if len(variables) > 1 else None)
        return fig
    else:
        raise ValueError("Tipo de gráfico no válido")
        
        
# Cargar Dataframes
dataframes = load_dataframes()
# Seleccionar dataframe
df_name = st.selectbox('Seleccione un dataframe', list(dataframes.keys()))

# Mostrar resumen del dataframe
df = dataframes[df_name]
st.dataframe(df)

# Mostrar nombres de las columnas
columnas = list(df.columns)

# Mostrar nombres de las columnas y su descripción
if st.button("Mostrar descripción de las columnas"):
    column_descriptions = {
        'Afiliados Edad Sexo Cotizacion': {
            'Grupo Numero': 'Número de grupo de afiliados',
            'Grupo Descripcion': 'Descripción del grupo de afiliados',
            'Sexo': 'Sexo de los afiliados',
            'Rango de Edad': 'Rango de edad de los afiliados',
            'Cantidad Afiliados': 'Cantidad de afiliados en el grupo'
        },
        'Tabla Regiones': {
            'Región Geográfica/2': 'Región geográfica',
            'Región Salud': 'Región de salud',
            'Provincia': 'Provincia'
        },
        'Datos Regionales Cotizacion': {
              "Total general": "Número total de afiliados en la región.",
              "Total Región Distrito Nacional a San Juan de la Maguana": "Número total de afiliados en cada provincia o distrito.",
              "No Especificada": "Número de afiliados cuya ubicación no está especificada.",
              "Year": "Año al que se refiere el registro.",
              "Month": "Mes al que se refiere el registro.",
              "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
              "Cotizante": "Tipo de afiliado (cotizante o no cotizante)."

        },
        'Region Salud Total': {
          "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "Year": "Año al que se refiere el registro.",
          "Month": "Mes al que se refiere el registro.",
          "Total general a Total VI - El Valle": "Número total de afiliados en cada región de salud.",
          "Cotizante": "Tipo de afiliado (cotizante o no cotizante)."
         },
        'Region Geografica Total Combinado': {
          "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "Year": "Año al que se refiere el registro.",
          "Month": "Mes al que se refiere el registro.",
          "Total general a Total Región Sur": "Número total de afiliados en cada región geográfica.",
          "Cotizante": "Tipo de afiliado (cotizante o no cotizante)."
         },
        'SFS Regimen Sexo Porcentaje Tasa': {
           "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "SFS_Total, SFS_Hombres, SFS_Mujeres": "Número total de afiliados en el Seguro Familiar de Salud (SFS) según sexo.",
          "Reg_Subsidiado_Total, Reg_Subsidiado_Hombres, Reg_Subsidiado_Mujeres": "Número total de afiliados en el régimen subsidiado según sexo.",
          "RC_Total, RC_Hombres, RC_Mujeres": "Número total de afiliados en el régimen contributivo según sexo.",
          "Year": "Año al que se refiere el registro.",
          "Month": "Mes al que se refiere el registro.",
          "Poblacion Total proyectada": "Población total proyectada.",
          "Porcentaje de Población Cubierta por el SFS": "Porcentaje de la población cubierta por el SFS.",
          "Total Seguro Familiar de Salud": "Número total de personas cubiertas por el Seguro Familiar de Salud.",
          "Reg_Subsidiado, Reg_Contributivo": "Número total de personas en el régimen subsidiado y contributivo, respectivamente.",
          "Tasa_Dep_Regimen_Subsidiado, RC_Tasa_Dependencia, RC_Tasa_Dependencia_Directa": "Tasas de dependencia de los diferentes regímenes."
        },
        'Financiamiento Dispersado TipoARS postMes': {
          "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "Total_Capitas_Dispersadas, Total_Capitas_Dispersada_mes, Total_Capitas_Dispersada_posterior": "Total de capitas dispersadas en total, en el mes actual y en meses posteriores, respectivamente.",
          "Titulares_Total_capitas, Titulares_Dispersadas_mes_capitas, Titulares_Dispersadas_posterior_capitas": "Número total de titulares de capitas, dispersados en el mes actual y en meses posteriores, respectivamente.",
          "Dependientes_Total_capitas, Dependientes_Dispersadas_mes_capitas, Dependientess_Dispersadas_posterior_capitas": "Número total de dependientes de capitas, dispersados en el mes actual y en meses posteriores, respectivamente.",
          "Adicionales_Total_capitas, Adicionales_Dispersadas_mes_capitas, Adicionales_Dispersadas_posterior_capitas": "Número total de adicionales de capitas, dispersados en el mes actual y en meses posteriores, respectivamente.",
          "Year, Month": "Año y mes al que se refiere el registro.",
          "Total_Monto_Dispersadas, Total_Monto_Dispersada_mes, Total_Monto_Dispersada_posterior": "Monto total dispersado en total, en el mes actual y en meses posteriores, respectivamente.",
          "Tipo_de_ARS": "Tipo de Administradora de Riesgos de Salud (ARS)."
        },
        'Financiamiento Dispersado Salario': {
          "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "Total Empresas con aportes": "Número total de empresas con aportes.",
          "Recaudo SFS, Cuidado de la Salud, Estancias Infantiles, Subsidios, Comisión Operación SISALRIL, Cápita Adicional, Recargo por Atraso en pago de Facturas": "Montos relacionados con el financiamiento.",
          "Year, Month": "Año y mes al que se refiere el registro.",
          "Salario Mínimo Cotizable, Tope de Salario Mínimo Cotizable": "Montos relacionados con el salario mínimo cotizable y su tope.",
          "Total_Monto_Dispersadas": "Monto total dispersado.",
          "Total_Capitas_Titulares, Total_Capitas_Depend_Directos, Total_Capitas_Depend_Adicionales": "Número total de capitas de titulares, dependientes directos y dependientes adicionales, respectivamente.",
          "Monto_Dispersado_Total, Monto_Dispersado_Titulares, Monto_Dispersado_Dep_Directos, Monto_Dispersado_Dep_Adicionales": "Montos dispersados totales y por tipo de afiliado."
         },
        'FinanciamientoARS SaludPIB Regimen': {
          "Ano de Cobertura": "Año al que se refiere el registro.",
          "Total_Salud (A), PDSS_Subsidiado (A), PDSS_Contributivo (A), Otros_Planes_de_Salud (A)": "Montos relacionados con la salud en diferentes regímenes.",
          "PIB/Precios Corrientes (B)": "Producto Interno Bruto (PIB) a precios corrientes.",
          "Total en Relación al PIB (A/B), PDSS_Subsidiado en Relación al PIB (A/B), PDSS_Contributivo en Relación al PIB (A/B), Otros_Planes_de_Salud en Relación al PIB (A/B)": "Relación de los montos de salud con el PIB.",
          "Total Dispersado SFS, Régimen Contributivo, Régimen Subsidiado": "Montos dispersados y relacionados con los diferentes regímenes."
        },
        'PrestacionesPBS': {
           "Ano de Cobertura": "Año al que se refiere el registro.",
          "Total_Salud (A), PDSS_Subsidiado (A), PDSS_Contributivo (A), Otros_Planes_de_Salud (A)": "Montos relacionados con la salud en diferentes regímenes.",
          "PIB/Precios Corrientes (B)": "Producto Interno Bruto (PIB) a precios corrientes.",
          "Total en Relación al PIB (A/B), PDSS_Subsidiado en Relación al PIB (A/B), PDSS_Contributivo en Relación al PIB (A/B), Otros_Planes_de_Salud en Relación al PIB (A/B)": "Relación de los montos de salud con el PIB.",
          "Total Dispersado SFS, Régimen Contributivo, Régimen Subsidiado": "Montos dispersados y relacionados con los diferentes regímenes."
       },
        'Ingresos Gastos Siniestralidad': {
          "Periodo de Cobertura": "Periodo de tiempo al que se refiere el registro.",
          "Ingresos en Salud_RC, Gasto en Salud_RC": "Montos de ingresos y gastos en salud para el Régimen Contributivo.",
          "Porcentaje (%) de Siniestralidad_RC": "Porcentaje de siniestralidad para el Régimen Contributivo.",
          "Ingresos en Salud_OP, Gasto en Salud_OP": "Montos de ingresos y gastos en salud para el Régimen de Pensionados y Jubilados.",
          "Porcentaje (%) de Siniestralidad_OP": "Porcentaje de siniestralidad para el Régimen de Pensionados y Jubilados.",
          "Year, Month": "Año y mes al que se refiere el registro."
      },
        'Ingresos Gastos Siniestralidad Anual': {
          "Ano de Cobertura": "Año al que se refiere el registro.",
          "Ingresos ARS Total_RC, Ingresos ARS Autogestion_RC, Ingresos ARS Privada_RC, Ingresos ARS Publica_RC": "Montos de ingresos de las ARS en diferentes categorías (Régimen Contributivo).",
          "Gastos ARS Total_RC, Gastos ARS Autogestion_RC, Gastos ARS Privada_RC, Gastos ARS Publica_RC": "Montos de gastos de las ARS en diferentes categorías (Régimen Contributivo).",
          "Siniestralidad ARS Total_RC, Siniestralidad ARS Autogestion_RC, Siniestralidad ARS Privada_RC, Siniestralidad ARS Publica_RC": "Siniestralidad de las ARS en diferentes categorías (Régimen Contributivo).",
          "Ingresos ARS Total_OP, Ingresos ARS Autogestion_OP, Ingresos ARS Privada_OP, Ingresos ARS Publica_OP": "Montos de ingresos de las ARS en diferentes categorías (Régimen de Pensionados y Jubilados).",
          "Gastos ARS Total_OP, Gastos ARS Autogestion_OP, Gastos ARS Privada_OP, Gastos ARS Publica_OP": "Montos de gastos de las ARS en diferentes categorías (Régimen de Pensionados y Jubilados).",
          "Siniestralidad ARS Total_OP, Siniestralidad ARS Autogestion_OP, Siniestralidad ARS Privada_OP, Siniestralidad ARS Publica_OP": "Siniestralidad de las ARS en diferentes categorías (Régimen de Pensionados y Jubilados)."
     }
    }

    if df_name in column_descriptions:
        st.write('Descripción de las columnas:')
        st.write(column_descriptions[df_name])
    else:
        st.write('No se encontraron descripciones para las columnas de este DataFrame.')
        
        
# Definición de tipos de gráficos disponibles
tipos_graficos = {
    "Histograma": px.histogram,
    "Diagrama de dispersión": px.scatter,
    # Agrega más tipos de gráficos aquí si lo deseas
}

# Inicialización del tipo de gráfico seleccionado
tipo_grafico_seleccionado = st.selectbox("Seleccione el tipo de gráfico", list(tipos_graficos.keys()))
dataframe =df
# Obtener variables del dataframe
variables = list(dataframe.columns)

# Seleccionar variables para el gráfico
if tipo_grafico_seleccionado in ["Histograma", "Diagrama de dispersión"]:
    variable_x = st.selectbox("Seleccione la variable X", variables)
else:
    variable_x = st.selectbox("Seleccione la variable X", variables)
    variable_y = st.selectbox("Seleccione la variable Y", variables)

# Filtrar datos (opcional)
filtros = {}
for variable in variables:
    valor_filtro = st.sidebar.text_input(f"Filtrar por {variable}", "")
    if valor_filtro != "":
        filtros[variable] = valor_filtro

# Aplicar filtros al DataFrame
for variable, valor_filtro in filtros.items():
    dataframe = dataframe[dataframe[variable] == valor_filtro]

# Generar gráfico
try:
    fig = generar_grafico(dataframe, tipo_grafico_seleccionado, [variable_x, variable_y])
    st.plotly_chart(fig)
except ValueError as e:
    st.error(str(e))