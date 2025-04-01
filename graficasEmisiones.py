import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np


import streamlit as st

def mostrar_kpi_totales(df, kpi_name, column_name, color="#222"):
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return
    
    if column_name not in df.columns:
        st.error(f"La columna '{column_name}' no se encuentra en el dataframe.")
        return

    total_value = df[column_name].sum()

    st.markdown(
        f"""
        <div style="text-align:center; background-color:{color}; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">{kpi_name}</p>
            <p style="color:white; font-size:20px; margin:5px 0;"><b>{total_value:,.2f}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )


#GRAFICAS EMISIONES

def tarjeta_pais_mayor_emision(df):
    # Obtener el país con más emisiones
    pais_mayor = df.groupby("Country", as_index=False)["Value"].sum().nlargest(1, "Value")

    # Obtener el nombre del país y el valor de las emisiones
    pais = pais_mayor.iloc[0]["Country"]
    emisiones = pais_mayor.iloc[0]["Value"]

    # Mostrar la tarjeta con el mismo estilo
    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">País con más Emisiones</p>
            <p style="color:white; font-size:24px; margin:5px 0;"><b>{pais}</b></p>
            <p style="color:white; font-size:18px; margin:5px 0;"><b>{emisiones:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def tarjeta_emisiones_ultimos_5_anios(df):
    # Filtrar los datos de los últimos 5 años
    anios_recientes = df[df["Year"] >= df["Year"].max() - 5]
    
    # Calcular las emisiones totales en los últimos 5 años
    emisiones_totales_recientes = anios_recientes["Value"].sum()

    # Mostrar la tarjeta con el estilo
    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">Emisiones Totales (Últimos 5 Años)</p>
            <p style="color:white; font-size:24px; margin:5px 0;"><b>{emisiones_totales_recientes:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def tarjeta_pais_mayor_reduccion(df):
    # Calcular la reducción de emisiones de cada país (último año - primer año)
    df_pivot = df.pivot_table(index="Country", columns="Year", values="Value")
    df_pivot["reduccion"] = df_pivot.iloc[:, -1] - df_pivot.iloc[:, 0]
    
    # Seleccionar el país con mayor reducción
    pais_mayor_reduccion = df_pivot["reduccion"].idxmin()
    reduccion = df_pivot.loc[pais_mayor_reduccion, "reduccion"]

    # Mostrar la tarjeta con el estilo
    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">País con Mayor Reducción de Emisiones</p>
            <p style="color:white; font-size:24px; margin:5px 0;"><b>{pais_mayor_reduccion}</b></p>
            <p style="color:white; font-size:18px; margin:5px 0;"><b>{reduccion:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def tarjeta_emisiones_promedio_global(df):
    # Excluir los valores nulos en la columna 'Value'
    df_sin_nulos = df.dropna(subset=['Value'])

    # Calcular las emisiones promedio globales
    emisiones_promedio = df_sin_nulos["Value"].mean()

    # Mostrar la tarjeta con el estilo
    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">Emisiones Promedio Globales</p>
            <p style="color:white; font-size:24px; margin:5px 0;"><b>{emisiones_promedio:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )


def grafico_tendencia_emisiones(df):
    df_agrupado = df.groupby("Year", as_index=False)["Value"].sum()
    fig = px.line(df_agrupado, x="Year", y="Value", title="Tendencia de Emisiones Globales", markers=True)
    st.plotly_chart(fig, use_container_width=True)

def grafico_emisiones_paises(df):
    df_agrupado = df.groupby("Country", as_index=False)["Value"].sum()
    df_top10 = df_agrupado.nlargest(10, "Value")  # Seleccionar los 10 países con mayores emisiones

    fig = px.bar(df_top10, x="Country", y="Value", title="Top 10 Países con Mayores Emisiones",
                 labels={"Value": "Total de Emisiones"}, color="Value", color_continuous_scale="Reds")

    st.plotly_chart(fig, use_container_width=True)


def grafico_mapa_emisiones(df):
    # Agrupar por país y sumar las emisiones
    df_agrupado = df.groupby(['Country', 'iso_alpha'], as_index=False)['Value'].sum()
    
    # Crear el mapa coroplético
    fig = px.choropleth(df_agrupado, locations='iso_alpha', locationmode='ISO-3',
                        color='Value', hover_name='Country',
                        title='Mapa de Emisiones de CO₂ por País (Suma Total)',
                        color_continuous_scale='Reds')
    
    # Ajustar el tamaño del mapa
    fig.update_layout(height=700, width=1200)  
    
    st.plotly_chart(fig, use_container_width=True)  # Ocupa el ancho disponible en Streamlit


def mostrar_kpi_total_emisiones(df):
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return

    total_emisiones = df["Value"].sum()

    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">Total de Emisiones de CO₂</p>
            <p style="color:white; font-size:20px; margin:5px 0;"><b>{total_emisiones:,.2f} toneladas</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )



#GRAFICAS CONSUMO


def tarjeta_suma_consumo_por_energia(df):
    # Agrupar los datos por 'Energy Type' y calcular la suma del consumo
    df_suma = df.groupby('Energy Type', as_index=False)['consumption (GWh)'].sum()
    
    # Ordenar los resultados de mayor a menor según el consumo
    df_suma = df_suma.sort_values(by='consumption (GWh)', ascending=False)
    
    # Generar una tarjeta para cada tipo de energía, de mayor a menor
    for index, row in df_suma.iterrows():
        energy_type = row['Energy Type']
        total_consumption = row['consumption (GWh)']
        
        st.markdown(
            f"""
            <div style="text-align:center; background-color:#222; padding:20px; 
                        border-radius:10px; width:220px; margin: 15px auto; 
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <p style="color:white; font-size:10px; margin:0;">Consumo Total de {energy_type}</p>
                <p style="color:white; font-size:20px; margin:5px 0;"><b>{total_consumption:,.2f} GWh</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

def mostrar_kpi_total_consumo(df):
    if df.empty:
        st.warning("No hay datos disponibles después de aplicar los filtros.")
        return

    total_consumo = df["consumption (GWh)"].sum()

    st.markdown(
        f"""
        <div style="text-align:center; background-color:#222; padding:20px; 
                    border-radius:10px; width:220px; margin: 15px auto; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <p style="color:white; font-size:10px; margin:0;">Total de Consumo (GWh)</p>
            <p style="color:white; font-size:20px; margin:5px 0;"><b>{total_consumo:,.2f}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def grafico_tendencia_pais(df):
    # Agrupar por Year y Energy Type, sumando los valores de consumption (GWh)
    df_agg = df.groupby(['Year', 'Energy Type'], as_index=False)['consumption (GWh)'].sum()

    # Crear el gráfico de líneas (sin sombras)
    fig = px.line(df_agg, x='Year', y='consumption (GWh)', color='Energy Type',
                  title='Tendencia del Consumo de Energía por Fuente', markers=True)

    # Mostrar el gráfico
    st.plotly_chart(fig)


def grafico_distribucion_fuente(df):
    fig = px.treemap(df, path=['Energy Type'], values='consumption (GWh)',
                     title='Distribución de Consumo por Energy Type',
                     color='consumption (GWh)', color_continuous_scale='viridis')
    fig.update_layout(coloraxis_colorbar=dict(orientation='h', yanchor='bottom', y=-0.2))
    fig.update_layout(legend_orientation='h', legend=dict(y=-0.3))
    st.plotly_chart(fig)

def comparacion_paises(df):
    fig = px.bar(df, x='Country', y='consumption (GWh)', color='Energy Type',
                 title='Comparación de Consumo entre Países',
                 labels={'consumption (GWh)': 'Consumo (GWh)'}, barmode='stack')
    st.plotly_chart(fig)

def consumo_total_anual(df):
    df_agrupado = df.groupby('Year', as_index=False)['consumption (GWh)'].sum()
    fig = px.line(df_agrupado, x='Year', y='consumption (GWh)',
                  title='Consumo Total de Energía a lo Largo del Tiempo', markers=True)
    st.plotly_chart(fig)


#GRAFICAS PRODUCCION

def grafico_tendencia_produccion(df):
    # Agrupar por Year y Product, sumando los valores de Value
    df_agg = df.groupby(['Year', 'Product'], as_index=False)['Value'].sum()

    # Crear el gráfico de líneas
    fig = px.line(df_agg, x='Year', y='Value', color='Product',
                  title='Tendencia de Producción de Electricidad por Fuente', markers=True)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

def tarjeta_tendencia_renovable(df):
    # Lista de energías renovables según el dataset
    energias_renovables = ["Geothermal", "Hydro", "Solar", "Other Renewables", "Combustible Renewables"]

    # Filtrar solo energías renovables
    df_renovable = df[df["Product"].isin(energias_renovables)]

    # Agrupar por tipo de energía y año, sumando los valores de producción
    df_agg = df_renovable.groupby(['Year', 'Product'], as_index=False)['Value'].sum()

    # Analizar la tendencia por cada tipo de energía renovable
    for energia in df_agg["Product"].unique():
        df_tipo = df_agg[df_agg["Product"] == energia]

        # Calcular la pendiente de la tendencia usando regresión lineal
        if len(df_tipo) > 1:
            years = df_tipo["Year"].values
            valores = df_tipo["Value"].values
            pendiente = np.polyfit(years, valores, 1)[0]  # Coeficiente de inclinación

            tendencia = "aumentando 📈" if pendiente > 0 else "disminuyendo 📉"
        else:
            tendencia = "No suficiente información"

        # Calcular la producción total de la energía renovable
        total_produccion = df_tipo["Value"].sum()

        # Generar la tarjeta
        st.markdown(
            f"""
            <div style="text-align:center; background-color:#222; padding:20px; 
                        border-radius:10px; width:250px; margin: 15px auto; 
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <p style="color:white; font-size:10px; margin:0;">Producción Total de {energia}</p>
                <p style="color:white; font-size:20px; margin:5px 0;"><b>{total_produccion:,.2f} GWh</b></p>
                <p style="color:white; font-size:10px; margin:0;">Tendencia: <b>{tendencia}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

def grafico_tendencia_total(df):
    # Agrupar por Year y sumar los valores de Value
    df_agg = df.groupby('Year', as_index=False)['Value'].sum()

    # Crear el gráfico de líneas
    fig = px.line(df_agg, x='Year', y='Value',
                  title='Tendencia Total de Producción de Electricidad', markers=True)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

def comparacion_produccion_paises(df):
    fig = px.bar(df, x='Country', y='Value', color='Product',
                 title='Comparación de Producción entre Países', barmode='stack')
    st.plotly_chart(fig)

def participacion_fuentes(df):
    fig = px.pie(df, names='Product', values='Value',
                 title='Participación de Cada Energy Type')
    st.plotly_chart(fig)

def mapa_emisiones(df):
    if df.empty:
        st.warning("No hay datos disponibles.")
        return
    
    # Agrupar por país y sumar las emisiones totales
    df_grouped = df.groupby(["iso_alpha", "Country"], as_index=False)["Value"].sum()

    # Crear el mapa de calor con Plotly
    fig = px.choropleth(
        df_grouped,
        locations="iso_alpha",  # Código de país en formato ISO Alpha-3
        color="Value",
        hover_name="Country",
        color_continuous_scale="Reds",
        title="Emisiones Totales de CO₂ por País",
        projection="natural earth"
    )

    # Mostrar el mapa en Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_porcentaje_renovables(df):
    # Definir listas de energías renovables y no renovables
    renovables = ["Hydro", "Solar", "Wind", "Geothermal", "Other Renewables"]
    no_renovables = ["Coal-Peat and Manufactured Gases", "Oil and Petroleum Products", "Natural Gas", "Nuclear"]

    # Agrupar datos por año y tipo de energía
    df_agrupado = df.groupby(["Year", "Product"], as_index=False)["Value"].sum()

    # Calcular producción total por año
    total_por_anio = df_agrupado.groupby("Year")["Value"].sum()

    # Calcular producción renovable y no renovable
    renovable_por_anio = df_agrupado[df_agrupado["Product"].isin(renovables)].groupby("Year")["Value"].sum()
    no_renovable_por_anio = df_agrupado[df_agrupado["Product"].isin(no_renovables)].groupby("Year")["Value"].sum()

    # Crear dataframe de porcentajes
    df_porcentaje = pd.DataFrame({
        "Year": total_por_anio.index,
        "Renovables (%)": (renovable_por_anio / total_por_anio * 100).fillna(0),
        "No Renovables (%)": (no_renovable_por_anio / total_por_anio * 100).fillna(0)
    })

    # Transformar a formato largo para Plotly
    df_melted = df_porcentaje.melt(id_vars=["Year"], var_name="Tipo de Energía", value_name="Porcentaje")

    # Crear gráfico de barras agrupadas
    fig = px.bar(df_melted, x="Year", y="Porcentaje", color="Tipo de Energía",
                 barmode="group", title="Porcentaje de Producción de Electricidad: Renovables vs No Renovables",
                 labels={"Porcentaje": "Porcentaje (%)", "Year": "Año", "Tipo de Energía": "Fuente"},
                 color_discrete_map={"Renovables (%)": "#2ca02c", "No Renovables (%)": "#d62728"})  # Verde y rojo
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

def info_adicional_produccion():
    # Agregar descripción de la leyenda en Streamlit
    st.markdown(
        """
        **🔹 Energías Renovables:**  
        - Hydro (Hidráulica)  
        - Solar (Solar)  
        - Wind (Eólica)  
        - Geothermal (Geotérmica)  
        - Other Renewables
          (Otras renovables)  

        **🔸 Energías No Renovables:**  
        - Coal-Peat and Manufactured
          Gases (Carbón
            y gases manufacturados)  
        - Oil and Petroleum Products
          (Petróleo y derivados)  
        - Natural Gas (Gas Natural)  
        - Nuclear (Nuclear)  
        """, unsafe_allow_html=True
    )





#GRAFICOS INFERENCIAS
# Cargar datos

@st.cache_data
def calcular_porcentaje_co2(df):
    # Calcular el porcentaje de CO2 solo una vez y almacenarlo en caché
    df["% CO2"] = (df["total emissions CO2 (KgCo2)"] / df["total emissions CO2 (KgCo2)"].sum()) * 100
    return df

@st.cache_data
def grafico_barras(df):
    calcular_porcentaje_co2(df)
    st.subheader("Porcentaje de emisiones de CO₂ por producto")
    
    # Usar solo las columnas necesarias para la gráfica para optimizar rendimiento
    df_barras = df[['Product', '% CO2']]
    
    # Crear el gráfico de barras con solo los datos necesarios
    fig = px.bar(
        df_barras, x="Product", y="% CO2", text_auto=True, 
        title="Porcentaje de Emisiones de CO₂ por Producto",
        labels={"% CO2": "Porcentaje de CO₂", "Product": "Tipo de Producto"},
        color="% CO2", color_continuous_scale="Blues"
    )
    fig.update_layout(
        xaxis_title="Tipo de Producto",
        yaxis_title="Porcentaje de Emisiones CO₂",
        template="plotly_white",
        uniformtext_minsize=8, uniformtext_mode='hide'
    )
    st.plotly_chart(fig)

@st.cache_data
def grafico_treemap_colombia(df):
    st.subheader("Distribución de emisiones de CO₂ por producto en Colombia")
    
    # Filtrar solo los datos de Colombia
    df_colombia = df[df["Country"] == "Colombia"]
    
    # Calcular el porcentaje de CO2 en lugar de copiar el DataFrame
    df_colombia["% CO2"] = (df_colombia["total emissions CO2 (KgCo2)"] / df_colombia["total emissions CO2 (KgCo2)"].sum()) * 100
    
    # Crear el gráfico de treemap
    fig = px.treemap(
        df_colombia, path=["Product"], values="% CO2", 
        title="Distribución de Emisiones de CO₂ por Producto en Colombia",
        labels={"% CO2": "Porcentaje de CO₂"},
        color="% CO2", color_continuous_scale="Reds"
    )
    fig.update_layout(
        template="plotly_white",
        margin=dict(t=50, l=25, r=25, b=25)
    )
    st.plotly_chart(fig)

def tarjetas_total_co2(df):
    # Agrupar por Product y sumar el total de CO₂
    df_suma = df.groupby('Product', as_index=False)['total emissions CO2 (KgCo2)'].sum()
    df_suma = df_suma.sort_values(by='total emissions CO2 (KgCo2)', ascending=False)

    # Generar una tarjeta para cada producto
    for _, row in df_suma.iterrows():
        product = row['Product']
        total_co2 = row['total emissions CO2 (KgCo2)']

        st.markdown(
            f"""
            <div style="text-align:center; background-color:#222; padding:20px; 
                        border-radius:10px; width:250px; margin: 15px auto; 
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <p style="color:white; font-size:12px; margin:0;">Emisiones Totales de {product}</p>
                <p style="color:white; font-size:18px; margin:5px 0;"><b>{total_co2:,.2f} Kg CO₂</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )


def plot_emissions_percentage(df):
    # Calcular el total de emisiones CO2
    total_emissions = df['total emissions CO2 (KgCo2)'].sum()

    # Calcular el porcentaje de emisiones por cada Product
    df['Emissions Percentage'] = (df['total emissions CO2 (KgCo2)'] / total_emissions) * 100

    # Crear gráfico de barras vertical con Plotly
    fig = px.bar(df, 
                 x='Product', 
                 y='Emissions Percentage', 
                 title='Percentage of CO2 Emissions by Product', 
                 labels={'Emissions Percentage': 'Percentage of Total CO2 Emissions (%)'},
                 color='Product')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)


def plot_total_emissions_by_product(df):
    # Calcular el total de emisiones CO2 por producto y año
    df_total = df.groupby(['Year', 'Product'], as_index=False)['total emissions CO2 (KgCo2)'].sum()

    # Crear gráfico de líneas con Altair
    chart = alt.Chart(df_total).mark_line().encode(
        x='Year:O',  # Aseguramos que Year sea un eje ordinal
        y='total emissions CO2 (KgCo2)',
        color='Product',
        tooltip=['Year', 'Product', 'total emissions CO2 (KgCo2)']
    ).properties(
        title='Total CO2 Emissions by Product Over the Years'
    )

    # Mostrar el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)



# Función para generar el gráfico con producción total, consumo total y porcentaje de CO2
def plot_production_consumption_percentage(df):
    # Agrupar por año para obtener la suma de 'Value' y 'consumption (GWh)'
    df_yearly = df.groupby('Year', as_index=False)[['Value', 'consumption (GWh)', 'total emissions CO2 (KgCo2)']].sum()

    # Calcular el total de emisiones CO2 en el dataframe
    total_emissions = df['total emissions CO2 (KgCo2)'].sum()

    # Calcular el porcentaje de las emisiones de CO2 por año respecto al total
    df_yearly['CO2 Emissions Percentage'] = (df_yearly['total emissions CO2 (KgCo2)'] / total_emissions) * 100

    # Crear gráfico de barras para la producción total y consumo total
    fig = px.bar(df_yearly, 
                 x='Year', 
                 y=['Value', 'consumption (GWh)'], 
                 title='Total Production, Consumption, and CO2 Emissions Percentage by Year',
                 labels={'Value': 'Total Production', 'consumption (GWh)': 'Total Consumption (GWh)', 'Year': 'Year'},
                 barmode='group')

    # Añadir la línea de porcentaje de CO2 con un segundo eje Y
    fig.add_scatter(x=df_yearly['Year'], 
                    y=df_yearly['CO2 Emissions Percentage'], 
                    mode='lines+markers', 
                    name='CO2 Emissions Percentage', 
                    line=dict(color='red'),
                    yaxis="y2")  # Usamos el segundo eje Y

    # Configurar el segundo eje Y (porcentaje de CO₂)
    fig.update_layout(
        yaxis2=dict(
            title='CO2 Emissions Percentage (%)',
            overlaying='y',  # Superponer al primer eje Y
            side='right',  # Colocamos el eje en el lado derecho
            showgrid=False  # Opcional: quitar la cuadrícula del segundo eje Y
        ),
        xaxis=dict(title='Year'),
        yaxis=dict(title='Total Production / Consumption'),
        showlegend=True,
        legend=dict(
            x=1.05,  # Mover la leyenda a la derecha
            y=1,     # Alinear la leyenda al tope del gráfico
            traceorder='normal',  # Orden normal de trazas
            orientation='v',  # Mostrar la leyenda vertical
            bgcolor='rgba(255, 255, 255, 0)',  # Fondo transparente para la leyenda
            borderwidth=0  # Sin borde alrededor de la leyenda
        )
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)