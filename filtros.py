import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu 

 

def obtener_dataframe(pagina):
    if pagina == "Bienvenido":
        return None
    elif pagina == "Analisis de consumo":
        return pd.read_csv("/workspaces/Talent_Tech/df_consumo_final.csv")
    elif pagina == "Analisis de Producción":
        return pd.read_csv('/workspaces/Talent_Tech/df_produccion_final.csv')
    elif pagina == "Emisiones de CO2":
        return pd.read_csv('/workspaces/Talent_Tech/df_emisiones_final.csv')
    elif pagina == "Inferencias":
        return pd.read_csv("/workspaces/Talent_Tech/df_produccion_consumo_final.csv")

def filtros_laterales(pagina):
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
        df = obtener_dataframe(pagina)
        if df is None:
            st.sidebar.warning("No hay datos disponibles para esta página.")
            return None, {}, (None, None)

        st.sidebar.header("Filtros")

        # Guardar filtros en st.session_state para hacerlos reactivos
        if "filtros" not in st.session_state:
            st.session_state["filtros"] = {}

        if "year_range" not in st.session_state:
            st.session_state["year_range"] = (None, None)

        filtros = st.session_state["filtros"]
        year_range = st.session_state["year_range"]

        if "Country" in df.columns:
            paises = df["Country"].dropna().unique()
            filtros["Country"] = st.sidebar.multiselect(
                f"Seleccionar País ({pagina})",
                options=paises,
                #default=paises[:5],
                key=f"filtro_pais_{pagina}"
            )

        if "Year" in df.columns:
            min_year, max_year = int(df["Year"].min()), int(df["Year"].max())
            year_range = st.sidebar.slider(
                "Seleccionar Rango de Años",
                min_value=min_year, max_value=max_year,
                value=(min_year, max_year),
                key=f"filtro_year_{pagina}"
            )
            filtros["Year"] = year_range

        st.session_state["filtros"] = filtros
        st.session_state["year_range"] = year_range

        return df, filtros, year_range

def aplicar_filtros(df, filtros, year_range):
    if df is None:
        return None
    df_filtrado = df.copy()

    for col, valores in filtros.items():
        if col == "Year" and year_range[0] is not None:
            df_filtrado = df_filtrado[
                (df_filtrado["Year"] >= year_range[0]) & (df_filtrado["Year"] <= year_range[1])
            ]
        elif valores:
            df_filtrado = df_filtrado[df_filtrado[col].isin(valores)]
    
    return df_filtrado

