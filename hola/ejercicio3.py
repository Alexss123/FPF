import streamlit as st
import numpy as np

# Crear un array con los números del 1 al 100
numeros = np.arange(1, 101)

# Calcular la suma de los números
suma = np.sum(numeros)

# Calcular la media de los números
media = np.mean(numeros)

# Mostrar los resultados en la aplicación de Streamlit
st.title("Array de Números del 1 al 100")
st.write("Array:", numeros)
st.write("Suma de todos los números:", suma)
st.write("Media de todos los números:", media)
