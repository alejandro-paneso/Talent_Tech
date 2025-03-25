import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np

def aplicar_filtros(df, dynamic_filters, year_range):
    # Si dynamic_filters es None, simplemente devuelve el DataFrame sin filtrar
    if not dynamic_filters:
        return df

    # Aplicar los filtros dinámicos
    for col, valores in dynamic_filters.items():
        if valores:  # Solo filtra si hay valores seleccionados
            df = df[df[col].isin(valores)]
    
    # Aplicar el filtro de año
    if year_range and isinstance(year_range, (list, tuple)) and len(year_range) == 2:
        df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

    return df


def grafico_value_por_year(df):
    """
    Genera un gráfico de líneas con la evolución de las emisiones de CO₂ por año.
    """
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return
    
    df_agrupado = df.groupby("Year", as_index=False)["Value"].sum()

    fig = px.line(
        df_agrupado, x="Year", y="Value",
        title="Evolución Total de Emisiones de CO₂ por Año",
        labels={"Value": "Emisiones Totales (toneladas per cápita)", "Year": "Año"}
    )
    
    st.plotly_chart(fig, use_container_width=True)

def mostrar_kpi_total_emisiones(df):
    """
    Muestra un KPI con la suma total de emisiones en un diseño atractivo.
    """
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return

    total_emisiones = df["Value"].sum()

    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:16px; margin:0;">Total de Emisiones de CO₂</p>
            <p style="color:white; font-size:32px; margin:5px 0;"><b>{total_emisiones:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def grafico_barras_emisiones(df):
    """
    Genera un gráfico de barras horizontal con los países ordenados de mayor a menor
    según la suma total de emisiones.
    """
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return

    df_agrupado = df.groupby("Country", as_index=False)["Value"].sum().sort_values(by="Value", ascending=False)

    fig = px.bar(
        df_agrupado,
        y="Country",
        x="Value",
        orientation="h",
        title="Total de Emisiones por País",
        labels={"Value": "Total Emisiones", "Country": "País"},
        text_auto=".2s"
    )

    fig.update_layout(
        height=600,
        width=900,
        yaxis=dict(categoryorder="total ascending"),
        xaxis=dict(title="Total Emisiones")
    )

    st.plotly_chart(fig, use_container_width=True)
