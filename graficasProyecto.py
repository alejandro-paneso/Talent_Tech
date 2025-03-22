import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
from vistas import *
from filtros import *
from InterfazProyecto import *

import streamlit as st
import plotly.express as px

def grafico_value_por_year(df):
    if df.empty:
        st.warning("No hay datos disponibles en el DataFrame.")
        return
    
    # Agrupar por año y sumar los valores
    df_agrupado = df.groupby('Year', as_index=False)['Value'].sum()

    # Crear gráfico de líneas
    fig = px.line(df_agrupado, x='Year', y='Value',
                  title="Evolución Total de Emisiones de CO₂ por Año",
                  labels={"Value": "Emisiones Totales de CO₂ (toneladas per cápita)", "Year": "Año"})
    
    st.plotly_chart(fig)

def grafico_suma_value_por_year(df, dynamic_filters, anio_to_filter):
    """
    Genera un gráfico de líneas mostrando la suma total de 'Value' por 'Year',
    aplicando filtros de país y año.

    Parámetros:
    - df: DataFrame con las columnas 'Year', 'Country' y 'Value'.
    - dynamic_filters: Objeto de DynamicFilters para filtrar por países.
    - anio_to_filter: Tupla con el rango de años seleccionados (min, max).
    """
    if df.empty:
        st.warning("No hay datos disponibles en el DataFrame.")
        return
    
    # Aplicar filtros dinámicos (selección de países)
    df_filtrado = dynamic_filters.apply(df)

    # Filtrar por rango de años
    df_filtrado = df_filtrado[(df_filtrado['Year'] >= anio_to_filter[0]) & (df_filtrado['Year'] <= anio_to_filter[1])]

    if df_filtrado.empty:
        st.warning("No hay datos disponibles para los filtros seleccionados.")
        return

    # Agrupar por año y sumar los valores de emisiones
    df_agrupado = df_filtrado.groupby('Year', as_index=False)['Value'].sum()

    # Crear gráfico de líneas
    fig = px.line(df_agrupado, x='Year', y='Value',
                  title="Evolución Total de Emisiones de CO₂ por Año",
                  labels={"Value": "Emisiones Totales de CO₂ (toneladas per cápita)", "Year": "Año"})
    
    st.plotly_chart(fig)

def display_kpi_card(state='Texas', value=29.0, unit='M', change=367, change_unit='K'):
    st.markdown(
        f"""
        <div style="text-align:center; background-color:#333; padding:20px; border-radius:10px; width:200px; margin: 15px;">
            <p style="color:white; font-size:16px; margin:0;">{state}</p>
            <p style="color:white; font-size:32px; margin:5px 0;"><b>{value} {unit}</b></p>
            <p style="color:#4CAF50; font-size:16px; margin:0;">&#x2191; {change} {change_unit}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    return display_kpi_card

def calculate_population_difference():
    st.write("Otro grafico parte 1")

def generate_dummy_data():
    years = np.arange(2000, 2025)  # Años de ejemplo
    categories = ['A', 'B', 'C', 'D', 'E']  # Categorías ficticias
    data = []
    for year in years:
        for category in categories:
            data.append({
                'Year': year,
                'Category': category,
                'Value': np.random.randint(1, 100)  # Valores aleatorios
            })
    return pd.DataFrame(data)

def make_heatmap(input_y='Year', input_x='Category', input_color='Value', input_color_theme='blues'):
    input_df = generate_dummy_data()
    heatmap = alt.Chart(input_df).mark_rect().encode(
        y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
        x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
        color=alt.Color(f'max({input_color}):Q',
                         legend=None,
                         scale=alt.Scale(scheme=input_color_theme)),
        stroke=alt.value('black'),
        strokeWidth=alt.value(0.25),
    ).properties(width=900
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    )
    return heatmap
