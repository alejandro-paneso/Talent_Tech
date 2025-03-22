import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu 
import numpy as np
import matplotlib.pyplot as plt
from graficasProyecto import *
from vistas import *
from filtros import *
from InterfazProyecto import *

from streamlit_dynamic_filters import DynamicFilters

df_produccion = pd.read_csv('/workspaces/Talent_Tech/produccion_limpio.csv')
df_emisiones = pd.read_csv('/workspaces/Talent_Tech/emisiones_limpio.csv')
#df_consumo = pd.read_csv('/workspaces/Talent_Tech/consumo_limpio.csv')

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
        col = st.columns((1.5, 4.5, 2), gap='large')
        with col[0]:
            display_kpi_card()
            display_kpi_card()
        with col[1]:
            st.write("Este es el contenedor exterior.")
            display_kpi_card()
            make_heatmap()
            calculate_population_difference()
        with col[2]:
            st.write('''
                        - Inserte links: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
                        - :orange[**Otro titulo*]: Otra inofmracion util
                        - :orange[**Titulo util**]: Información util
                        ''')                


def vista_emisiones(df_emisiones):
    st.title("Emisiones de CO2")
    st.write("Bienvenid a emisiones")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")
    with st.container():
        col = st.columns((1.5, 4.5, 2), gap='large')
        with col[0]:
            st.write("Bienvenido a emisiones")
        with col[1]:
            grafico_value_por_year(df_emisiones)
            grafico_suma_value_por_year(df_emisiones)
            #grafico_suma_value_por_year2(df_emisiones,dynamic_filters,anio_to_filter)

def vista_inferencias():
    st.title("Inferencias")
    st.write("Bienvenido a nuestro proyeto")
    st.write("Usa el menú a la izquierda para navegar por nuestro analisis")