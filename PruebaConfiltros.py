import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df_consumo = pd.read_csv("consumo_limpio.csv")
st.title("Análisis del Consumo de Energía")
# 🔹 **Gráfica 1: Evolución del Consumo de Energía Global**
st.subheader("Evolución del Consumo de Energía Global")
fig1 = px.bar(
    df_consumo,
    x="Year",
    y="Consumo [GWh]",
    color="Fuente de Energía",
    barmode="stack"
)
fig1.update_layout(yaxis_title="Consumo de Energía (GWh)")
st.plotly_chart(fig1)

# 🔹 **Opciones de ordenamiento del Top 10 para la segunda gráfica**
order_option = st.radio("Ordenar el Top 10 por:", ["Total histórico", "Últimos 15 años"])

if order_option == "Últimos 15 años":
    recent_years = df_consumo["Year"].max() - 14
    df_filtered = df_consumo[df_consumo["Year"] >= recent_years]
else:
    df_filtered = df_consumo

# 🔹 **Obtener los 10 países con mayor consumo según la opción elegida**
top_countries = df_filtered.groupby('Country')['Consumo [GWh]'].sum().nlargest(10)
top_countries_sorted = top_countries.sort_values(ascending=False).index

# 🔹 **Renombrar con números para mostrar ranking**
top_countries_display = [f"{i+1}. {country}" for i, country in enumerate(top_countries_sorted)]

# 🔹 **Selector de país en el Top 10**
selected_country_display = st.selectbox("Selecciona un país del Top 10", top_countries_display)
selected_country = selected_country_display.split(". ")[1]  # Extraer el nombre real del país

# 🔹 **Filtrar los datos para el país seleccionado**
filtered_df = df_consumo[df_consumo['Country'] == selected_country]

# Reordenar las fuentes de energía por consumo total en el país seleccionado
energy_order = filtered_df.groupby("Fuente de Energía")["Consumo [GWh]"].sum().sort_values(ascending=False).index
filtered_df["Fuente de Energía"] = pd.Categorical(filtered_df["Fuente de Energía"], categories=energy_order, ordered=True)
