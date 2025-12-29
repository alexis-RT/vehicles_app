import pandas as pd
import streamlit as st
import plotly.express as px

cars_data = pd.read_csv('vehicles_us.csv')

st.header("PLATAFORMA DE VENTA DE VEHÍCULOS")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_data = car_data.dropna(
    subset=['odometer', 'price'])  # eliminar valores nulos
hist_button = st.checkbox('Construir histograma')  # crear un botón
color_options = ["condition", "fuel", "transmission"]
selected_color = st.selectbox(
    "Selecciona la condicion del vehiculo que quieres observar:", color_options)

if hist_button:  # si se presiona el boton

    st.write(
        'Histograma que muestra la distribución del kilometraje de los coches')

    # crear un histograma
    fig = px.histogram(hist_data, x="odometer",
                       y="price", color=selected_color)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# GRÁFICO DE DISPERSIÓN
# botón para gráfico de dispersión
disp_graf_button = st.checkbox('Mostrar grafico de dispersión')

color_options = ["fuel", "transmission", "condition", "type"]
selected_color = st.selectbox("Selecciona la condicion del vehiculo que quieres observar:",
                              color_options)

if disp_graf_button:
    st.write(
        'Creación de un gráfico de dispersión para la relacion entre el kilometraje y el precio de los coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price", color=selected_color)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
print(cars_data.columns)
print(cars_data.head())
