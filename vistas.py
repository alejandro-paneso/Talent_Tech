import streamlit as st
import plotly.express as px
from filtros import filtros_laterales, aplicar_filtros
from graficasEmisiones import *
import matplotlib.pyplot as plt



df_produccion = pd.read_csv('/workspaces/Talent_Tech/df_produccion_final.csv')
df_emisiones = pd.read_csv('/workspaces/Talent_Tech/df_emisiones_final.csv')
df_consumo = pd.read_csv("/workspaces/Talent_Tech/df_consumo_final.csv")
df_unificado = pd.read_csv("/workspaces/Talent_Tech/df_produccion_consumo_final.csv")

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
    #st.title("Análisis de consumo")
    filtros_laterales("Análisis de consumo")
    with st.container():
        col = st.columns((2, 7), gap='large')
        with col[0]:
            mostrar_kpi_totales(df_consumo, "Total de Consumo (GWh)", "consumption (GWh)", color="#222")
            tarjeta_suma_consumo_por_energia(df_consumo)
        with col[1]:
            grafico_distribucion_fuente(df_consumo)
            grafico_tendencia_pais(df_consumo)
            consumo_total_anual(df_consumo)

# Vista de producción
def vista_produccion():
    #st.title("Análisis de Producción")
    with st.container():
        col = st.columns((1.5, 6), gap='large')
        info_adicional_produccion()
    with col[0]:
        mostrar_kpi_totales(df_produccion, "Total de Producción", "Value", "#222")
        tarjeta_tendencia_renovable(df_produccion)
    with col[1]:
        grafico_tendencia_produccion(df_produccion)
        grafico_tendencia_total(df_produccion)
        grafico_porcentaje_renovables(df_produccion)
        #mapa_produccion(df_produccion)


# Vista de emisiones de CO2
def vista_emisiones():
    #st.title("Emisiones de CO2")
    with st.container():
        col = st.columns((2, 2, 2,2,2,2), gap='large')
        with col[0]:
            mostrar_kpi_totales(df_emisiones, "Total de Emisiones de CO₂ (Ton)", "Value", "#222")
        with col[1]:
            tarjeta_pais_mayor_emision(df_emisiones)
        with col[2]:
            tarjeta_emisiones_promedio_global(df_emisiones)
        with col[3]:
            tarjeta_pais_mayor_reduccion(df_emisiones)
        with col[4]:
            tarjeta_emisiones_promedio_global(df_emisiones)
        with col[5]:
            tarjeta_emisiones_ultimos_5_anios(df_emisiones)
        grafico_tendencia_emisiones(df_emisiones)
        grafico_emisiones_paises(df_emisiones)
        grafico_mapa_emisiones(df_emisiones)


# Vista de inferencias
def vista_inferencias():
    with st.container():
        col = st.columns((6,1.5), gap='large')
    with col[0]:
        plot_emissions_percentage(df_unificado)
        plot_total_emissions_by_product(df_unificado)
        grafico_treemap_colombia(df_unificado) 
        plot_production_consumption_percentage(df_unificado)
    with col[1]:
        tarjetas_total_co2(df_unificado)
