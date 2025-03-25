import streamlit as st
import plotly.express as px
from filtros import filtros_laterales, aplicar_filtros
from graficasEmisiones import *

# Página principal
def pagina_principal():
    st.title("Página principal")
    st.write("Bienvenido a nuestro proyecto")

    with st.container():
        st.write("Este es el contenedor exterior.")
        with st.container():
            st.write("Este es el contenedor interior.")

# Vista de análisis de consumo
def vista_consumo():
    st.title("Análisis de consumo")
    st.write("Bienvenido a nuestro proyecto")
    filtros_laterales("Análisis de consumo")

# Vista de producción
def vista_produccion():
    st.title("Análisis de Producción")
    
    df_produccion, filtros, year_range = filtros_laterales("Análisis de Producción")
    df_filtrado = aplicar_filtros(df_produccion, filtros, year_range)

    with st.container():
        col = st.columns((1.5, 4.5, 2), gap='large')
        with col[0]:
            mostrar_kpi_total_emisiones(df_filtrado)
        with col[1]:
            st.write("Este es el contenedor exterior.")
            grafico_value_por_year(df_filtrado)
            grafico_barras_emisiones(df_filtrado)
        with col[2]:
            st.write('''
                - Inserte links: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
                - :orange[**Otro título**]: Otra información útil
                - :orange[**Título útil**]: Información útil
            ''')

# Vista de emisiones de CO2
def vista_emisiones():
    st.title("Emisiones de CO2")

    df_emisiones, filtros, year_range = filtros_laterales("Emisiones de CO2")  
    df_filtrado = aplicar_filtros(df_emisiones, filtros, year_range)  

    with st.container():
        col = st.columns((1.5, 4, 2.5), gap='large')
        with col[0]:
            mostrar_kpi_total_emisiones(df_filtrado)
        with col[1]:
            grafico_value_por_year(df_filtrado)
        with col[2]:
            grafico_barras_emisiones(df_filtrado)

# Vista de inferencias
def vista_inferencias():
    st.title("Inferencias")
    st.write("Bienvenido a nuestro proyecto")

    df_inferencias, filtros, year_range = filtros_laterales("Inferencias")
    df_filtrado = aplicar_filtros(df_inferencias, filtros, year_range)

    st.write("Usa el menú a la izquierda para navegar por nuestro análisis")
