import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu 
import numpy as np
import matplotlib.pyplot as plt

from streamlit_dynamic_filters import DynamicFilters

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 34, 45],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)


def pagina_principal():
    st.title("Pagina principal")
    st.write("Bienvenido a nuestro proyeto")
    with st.container():
        st.write("Este es el contenedor exterior.")
        with st.container():
            st.write("Este es el contenedor interior.")


def vista_consumo():
    st.title("Analisis de consumo")
    st.write("Bienvenido a nuestro proyeto")
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
    with st.container():
        col = st.columns((1.5, 4.5, 2), gap='medium')
        with col[1]:
            st.write("Este es el contenedor exterior.")
            with st.container():
                st.write("Este es el contenedor interior.")
                map_data = pd.DataFrame(
                np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                columns=['lat', 'lon'])
                st.map(map_data)



def vista_emisiones():
    st.title("Emisiones de CO2")
    st.write("Bienvenid a emisiones")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")

def vista_inferencias():
    st.title("Inferencias")
    st.write("Bienvenido a nuestro proyeto")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")

def filtros_laterales(pagina,df):
    if pagina == "Bienvenido":
        with st.sidebar:
            #seccion de filtros
            st.sidebar.title("Contexto")
            pagina_menu = option_menu(
                menu_title="Bienvenido",  #el valor puede ser none
                options=    ["Motivo 1",
                "Motivo 2",
                "Motivo 3",
                "Motivo 4",
                "Motivo 5"],
                default_index=-1, #valor seleccioando por defecto
                    # icons["house","book","envelope"], #traer nombres de iconos desde boostramp
                    #menu_icon="cast", #icono del encabezado
                
                )
    else:
        with st.sidebar:
            st.sidebar.title("Filtrar")
            st.write("Apply filters in any order 👇")
            dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])
            dynamic_filters.display_filters(location='sidebar')
            age_to_filter = st.slider('Age', min_value=0, max_value=100, value=(0, 100))
            st.sidebar.selectbox("Navegar",
            ["Bienvenido",
            "Analisis de consumo",
            "Analisis de producción",
            "Emisiones de CO2",
            "Inferencias"])
            #dynamic_filters.display_df()

