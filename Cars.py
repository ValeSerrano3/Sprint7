# Cargar todas las librerías
import pandas as pd
from scipy import stats as st
import streamlit as st  
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')



# Título de la app
st.title('Análisis Exploratorio de Datos de Vehículos')

# Mostrar tabla con las top 25 empresas con más anuncios
st.header('Top 25 Empresas con Más Anuncios')

# Contar los anuncios por modelo
top_companies = car_data['model'].value_counts().head(25).reset_index()

# Renombrar las columnas
top_companies.columns = ['Modelo', 'Cantidad de anuncios']

# Mostrar la tabla
st.dataframe(top_companies)

# Checkbox para mostrar histograma
if st.checkbox('Construir un histograma'):
    st.write('Histograma del odómetro (kilometraje)')
    # Crear histograma
    fig = px.histogram(car_data, x="odometer", title='Distribución del Odómetro')
    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para mostrar gráfico de dispersión
if st.checkbox('Construir gráfico de dispersión'):
    st.write('Gráfico de dispersión entre precio y kilometraje')
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title='Precio vs Kilometraje', color="fuel")
    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

# Checkbox para gráfico de barras
if st.checkbox('Construir gráfico de barras'):
    st.write('Cantidad de anuncios por tipo de combustible')
    # Crear gráfico de barras
    fuel_counts = car_data['fuel'].value_counts().reset_index()
    fuel_counts.columns = ['Tipo de Combustible', 'Cantidad de Anuncios']
    fig_bar = px.bar(fuel_counts, x='Tipo de Combustible', y='Cantidad de Anuncios', 
                     title='Cantidad de Anuncios por Tipo de Combustible', 
                     color='Tipo de Combustible')
    # Mostrar gráfico
    st.plotly_chart(fig_bar, use_container_width=True)

# Selector para elegir el modelo del coche
selected_model = st.selectbox('Selecciona un modelo de coche:', car_data['model'].unique())
# Selector para elegir la cantidad de cilindros
selected_cylinders = st.selectbox('Selecciona la cantidad de cilindros:', car_data['cylinders'].dropna().unique())

if selected_model and selected_cylinders:
    st.write(f'Precios a través de los años para: {selected_model} con {selected_cylinders} cilindros')
    # Filtrar los datos por el modelo y la cantidad de cilindros seleccionados
    filtered_data = car_data[(car_data['model'] == selected_model) & (car_data['cylinders'] == selected_cylinders)]
    # Crear gráfico de línea
    if not filtered_data.empty:
        fig_line = px.line(filtered_data, x='model_year', y='price', 
                           title=f'Precio a través de los años para {selected_model} con {selected_cylinders} cilindros', 
                           labels={'model_year': 'Año del Modelo', 'price': 'Precio'}, 
                           markers=True)
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.write('No hay datos disponibles para este modelo con la cantidad de cilindros seleccionada.')
