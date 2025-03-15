import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

#import plotly.express as px

# streamlit run graficandoStr.py
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

col = st.columns((1.5, 4.5, 2), gap='medium')

#barra de navegacion lateral
with st.sidebar:
    st.title('🏂 US Population Dashboard')
    
    year_list = list(['2020','2021'])[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    #df_selected_year = df_reshaped[df_reshaped.year == selected_year]
    #df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)



with col[0]:
    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))
    st.dataframe(dataframe.style.highlight_max(axis=0))
    fig, ax = plt.subplots()
    # Dibujar puntos
    ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
    # Guardar el gráfico en formato png
    plt.savefig('diagrama-dispersion.png')
    # Mostrar el gráfico
    plt.show()


with col[1]:
    st.markdown('#### Total Population')

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)


with col[2]:
    st.write(x, 'squared is', x * x)

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [6.30, -75.54],
    columns=['lat', 'lon'])

    st.map(map_data)

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text(f"{i}% complete")
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Rerun")