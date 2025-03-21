import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from streamlit_option_menu import option_menu
from streamlit_dynamic_filters import dynamic_filters
from vistas import *

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi']
}

df = pd.DataFrame(data)
#dynamic_filters = dynamic_filters(df, filters=['region', 'country', 'city', 'district'])


st.set_page_config(
    page_title="Proyecto Final Talento Tech",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''


#pip install streamlit pandas plotly
#pip install streamlit-option-menu
#pip install streamlit-dynamic-filters
#streamlit run interfazProyecto.py


#ENCABEZADO 
header = st.container()
header.title("Proyecto Final Talento Tech")
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
### Custom CSS for the sticky header
pagina = option_menu(
        menu_title=None,  #el valor puede ser none
        orientation = "horizontal",
        options=    ["Bienvenido",
        "Analisis de consumo",
        "Analisis de Producción",
        "Emisiones de CO2",
        "Inferencias"],
        icons = ["house","bi-bar-chart-steps","bi-bar-chart","bi-exclamation-circle-fill","bi-question-circle"],
        styles={"nav-link": {"font-size": "14px", "text-align": "center", "margin":"5px", "--hover-color": "gray"}}
        )

st.markdown(
    """
<style>
    .reportview-container {
        background-image:: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK8FJhao305nRI6EWMgw2hlzBbKLQhnUUgJQ&s");
    }
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: static;
        top: 2.875rem;
        background-color: RGBA(0,0,0,0);
        z-index: 999;
    }
    .fixed-header {
        border-bottom: 1px solid black;
    }
</style>
    """,
    unsafe_allow_html=True
)

#llamo la funcion de barra lateral
filtros_laterales(pagina,df)

if pagina == "Bienvenido":
    pagina_principal()
elif pagina == "Analisis de consumo":
    vista_consumo()
elif pagina == "Analisis de Producción":
    vista_produccion()
elif pagina == "Emisiones de CO2":
    vista_emisiones()
elif pagina == "Inferencias":
    vista_inferencias()