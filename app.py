import pandas as pd
import streamlit as st
import plotly.express as px

cars_data = pd.read_csv('vehicles_us.csv')

st.header("PLATAFORMA DE VENTA DE VEHÍCULOS")

clean_data = cars_data.dropna(
    subset=['odometer', 'price'])  # eliminar valores nulos
hist_button = st.checkbox('Construir histograma')  # crear un botón

if hist_button:  # si se presiona el boton

    color_options = ["condition", "fuel", "transmission"]
    selected_color = st.selectbox(
        "Selecciona la variable del vehiculo que quieres observar:", color_options)

    st.write(
        'Histograma que muestra la distribución del kilometraje de los coches')

    # crear un histograma
    fig = px.histogram(clean_data, x="odometer",
                       color=selected_color, opacity=0.7)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# GRÁFICO DE DISPERSIÓN
# botón para gráfico de dispersión
disp_graf_button = st.checkbox('Mostrar grafico de dispersión')

if disp_graf_button:
    color_options = ["fuel", "transmission", "condition", "type"]
    selected_color = st.selectbox("Selecciona la variable del vehiculo que quieres observar:",
                                  color_options)

    st.write(
        'Creación de un gráfico de dispersión para la relacion entre el kilometraje y el precio de los coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(clean_data, x="odometer",
                      y="price", color=selected_color, opacity=0.5)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
