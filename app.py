import streamlit as st  #importar libretia streamlit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn


st.title("Equipo Analej@beth")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))


st.dataframe(dataframe.style.highlight_max(axis=0))
#streamlit run app.py


st.write("<html><p>Esto es un parrafo</p><html>")


st.write("Hello word") #inprimimos en pantalla

# streamlit run app.py para correr el entorno virtual en el navegador


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

def main():
    st.title("Gráfico Básico con Streamlit")
    
    # Generar datos
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Crear figura
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Seno de x')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Gráfico de una función seno")
    ax.legend()
    
    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()


