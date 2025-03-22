import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu 
import numpy as np
import matplotlib.pyplot as plt
from graficasProyecto import *
from streamlit_dynamic_filters import DynamicFilters
from vistas import *


df_produccion = pd.read_csv('/workspaces/Talent_Tech/produccion_limpio.csv')
df_emisiones = pd.read_csv('/workspaces/Talent_Tech/emisiones_limpio.csv')
#df_consumo = pd.read_csv('/workspaces/Talent_Tech/consumo_limpio.csv')

def filtros_laterales(pagina):
    if pagina == "Bienvenido":
        df = df_produccion
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
    elif pagina == "Analisis de consumo":
        df = df_produccion
        # Obtener valores dinámicos de la columna 'year'
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        with st.sidebar:
            st.sidebar.title("Filtrar")
            st.write("Apply filters in any order 👇")
            dynamic_filters = DynamicFilters(df, filters=['Country', 'Balance', 'Product'])
            dynamic_filters.display_filters(location='sidebar')
            anio_to_filter = st.slider('Años', min_value=min_year, max_value=max_year, value=(min_year, max_year))
            #dynamic_filters.display_df()

    elif pagina == "Analisis de Producción":
        df = df_produccion
        # Obtener valores dinámicos de la columna 'year'
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        with st.sidebar:
            st.sidebar.title("Filtrar")
            st.write("Apply filters in any order 👇")
            dynamic_filters = DynamicFilters(df, filters=['Country', 'Balance', 'Product'])
            dynamic_filters.display_filters(location='sidebar')
            anio_to_filter = st.slider('Año', min_value=min_year, max_value=max_year, value=(min_year, max_year))
            #dynamic_filters.display_df()

    elif pagina == "Emisiones de CO2":
        df = df_emisiones
        # Obtener valores dinámicos de la columna 'year'
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        with st.sidebar:
            st.sidebar.title("Filtrar")
            st.write("Apply  👇")
            dynamic_filters = DynamicFilters(df, filters=['Country'])
            dynamic_filters.display_filters(location='sidebar')
            anio_to_filter = st.slider('Año', min_value=min_year, max_value=max_year, value=(min_year, max_year))
            dynamic_filters.display_df()

    elif pagina == "Inferencias":
        df = df_produccion
        # Obtener valores dinámicos de la columna 'year'
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        with st.sidebar:
            st.sidebar.title("Filtrar")
            #st.write("Apply filters in any order 👇")
            dynamic_filters = DynamicFilters(df, filters=['Country', 'Balance', 'Product'])
            dynamic_filters.display_filters(location='sidebar')
            anio_to_filter = st.slider('Año', min_value=0, max_value=100, value=(min_year, max_year))
            #dynamic_filters.display_df()

    else:
        df = df_produccion
        # Obtener valores dinámicos de la columna 'year'
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        with st.sidebar:
            st.sidebar.title("Filtrar")
            st.write("Apply filters in any order 👇")
            dynamic_filters = DynamicFilters(df, filters=['Country', 'Balance', 'Product'])
            dynamic_filters.display_filters(location='sidebar')
            anio_to_filter = st.slider('Año', min_value=0, max_value=100,value=(min_year, max_year))
            #dynamic_filters.display_df()
    

