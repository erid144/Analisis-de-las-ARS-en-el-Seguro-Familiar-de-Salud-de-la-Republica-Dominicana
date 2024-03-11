import sys
sys.path.append('src')
sys.path.append('models')
sys.path.append('data')
from librerias import *
from utils import *

# Mostrar un mensaje de bienvenida
st.title("¡Hola Mundo con Streamlit!")

# Mostrar un subtítulo
st.header("Probando Streamlit en Jupyter Notebook")

# Mostrar un párrafo informativo
st.write("Este es un simple código para verificar que Streamlit funciona correctamente en tu entorno.")

# Mostrar un botón
st.button("¡Presioname!")

# Mostrar un widget de selección
opcion = st.selectbox("Elige una opción:", ["Opción 1", "Opción 2", "Opción 3"])

# Mostrar un mensaje según la selección
st.write(f"Seleccionaste: {opcion}")

# Read the file to a dataframe using pandas
file ='data/Base_Creada/Afiliados_Edad_Sexo_Cotizacion.csv'
df = pd.read_csv(file)

# Create a section for the dataframe statistics
st.header('Statistics of Dataframe')
st.write(df)

# Create a section for the dataframe header
st.header('Header of Dataframe')
st.write(df.head())

# Create a section for matplotlib figure
st.header('Plot of Data')
