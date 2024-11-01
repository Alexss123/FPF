import streamlit as st
import numpy as np

# Título de la aplicación
st.title("Análisis de Números")

# Entrada de números por parte del usuario
numeros_input = st.text_input("Ingresa 10 números separados por comas (ejemplo: 5, 12, 7, ...):")

if numeros_input:
    # Convertir la entrada en una lista de números
    numeros = [int(num.strip()) for num in numeros_input.split(",")]

    # Asegurarse de que hay exactamente 10 números
    if len(numeros) != 10:
        st.error("Por favor, ingresa exactamente 10 números.")
    else:
        # Calcular la media
        media = np.mean(numeros)

        # Contar cuántos números son mayores, iguales y menores que 10
        mayores = sum(1 for num in numeros if num > 10)
        iguales = sum(1 for num in numeros if num == 10)
        menores = sum(1 for num in numeros if num < 10)

        # Mostrar resultados
        st.write(f"**Media:** {media}")
        st.write(f"**Números mayores que 10:** {mayores}")
        st.write(f"**Números iguales a 10:** {iguales}")
        st.write(f"**Números menores que 10:** {menores}")
