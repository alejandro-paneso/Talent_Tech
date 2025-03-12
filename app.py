import streamlit as st  #importar libretia streamlit

st.write("Hello word") #inprimimos en pantalla

# streamlit run app.py para en el navegador

import matplotlib.pyplot as plt
import numpy as np


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


