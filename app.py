import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    r"C:\Users\DELL\Documents\CARLOS\TRIPLE TEN\07-SPRINT - Herramientas de desarrollo de software\sprint-7\vehicles_us.csv"
)  # leer los datos

st.header('Tablero interactivo para visualización de datos de anuncios de venta de automóviles')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear un botón para dispersion
boton_dispersion = st.button('Ver gráfico de dispersión')

if boton_dispersion:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Gráfico de dispersión para el conjunto de datos de anuncios de venta de automóviles')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
