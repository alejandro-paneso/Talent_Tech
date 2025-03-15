import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Proyecto Final Talento Tech",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded")

#pip install streamlit pandas plotly
#pip install streamlit-option-menu
#streamlit run interfazProyecto.py
def pagina_principal():
    st.title("Pagina principal")
    st.write("Bienvenido a nuestro proyeto")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")

def vista_consumo():
    st.title("Analisis de consumo")
    st.write("Bienvenido a nuestro proyeto")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")
        #permitir que el archivo pueda ser ingresado por el usuario, defino la key 2 para poder llamar a ese archivo sin confundirnos entre archivos
        #archivo_cargado_consumo = st.file.uploader("Elige el archivo CSV de producción", type="csv")
        #permitamos que selecciones los ejes de un grafico
    """if archivo_cargado_consumo is not None:
        df_consumo =pd.read_csv(archivo_cargado_consumo)
        st.write("Elije la columna para el eje X:")
        eje_x = st.selectbox("Eje X",df_consumo.columns)
        eje_y = st.selectbox("Eje Y",df_consumo.columns)

        if st.button("Crear gráfico"):
            fig = px.bar(df_consumo, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)
    """

def vista_produccion():
    st.title("Analisis de Producción")
    st.write("Bienvenido a nuestro proyeto")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")
    #permitir que el archivo pueda ser ingresado por el usuario, defino la key 2 para poder llamar a ese archivo sin confundirnos entre archivos
    archivo_cargado_produccion = st.file.uploader("Elige el archivo CSV de producción", type="csv", key="2")
    #analizar si ya hay archivo para generar graficas
    if archivo_cargado_produccion is not None:
        df = pd.read_csv(archivo_cargado_produccion)
        st.write("Datos del archivo CSV:")
        st.write(df)
        st.write("Estadisticas descriptivas:")
        st.write(df.describe())

#ENCABEZADO 
header = st.container()
header.title("Proyecto Final Talento Tech")
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
### Custom CSS for the sticky header
pagina_menu_horizontal = option_menu(
        menu_title=None,  #el valor puede ser none
        orientation = "horizontal",
        options=    ["Bienvenido",
        "Analisis de consumo",
        "Analisis de producción",
        "Emisiones de CO2","Inferencias"],
        styles={"nav-link": {"font-size": "15px", "text-align": "center", "margin":"5px", "--hover-color": "gray"}}
        )
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: static;
        top: 2.875rem;
        background-color: RGBA(0,0,0,0);
        z-index: 999;
    }
    .fixed-header {
        border-bottom: 1px solid black;
    }
</style>
    """,
    unsafe_allow_html=True
)


#seccion de filtros
st.sidebar.title("Filtrar")
#creo el selector para navegar entre las paginas
pagina = st.sidebar.selectbox("",
    ["Bienvenido",
     "Analisis de consumo",
     "Analisis de producción",
     "Emisiones de CO2",
     "Inferencias"])

#probar cual de las dos se ve más bonita

        # icons["house","book","envelope"], #traer nombres de iconos desde boostramp
        #menu_icon="cast", #icono del encabezado
        #default_index=0, valor seleccioando por defecto
        #"""styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        #"icon": {"color": "orange", "font-size": "25px"}, 
        #"nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "green"},}"""

if pagina == "Bienvenido":
    pagina_principal()
elif pagina == "Analisis de consumo":
    vista_consumo()
elif pagina == "Analisis de producción":
    pagina_principal()
elif pagina == "Emisiones de CO2":
    pagina_principal()
elif pagina == "Inferencias":
    pagina_principal()