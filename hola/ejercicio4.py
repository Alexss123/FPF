import streamlit as st
import math

# Procedimiento para calcular el área de una circunferencia
def calcular_area(radio):
    return math.pi * radio ** 2

# Procedimiento para calcular el perímetro de una circunferencia
def calcular_perimetro(radio):
    return 2 * math.pi * radio

# Interfaz de Streamlit
st.title("Cálculo del Área y Perímetro de una Circunferencia")

# Entrada del radio
radio = st.number_input("Introduce el radio de la circunferencia:", min_value=0.0, step=0.1)

# Calcular y mostrar resultados
if radio > 0:
    area = calcular_area(radio)
    perimetro = calcular_perimetro(radio)
    st.write(f"Área: {area:.2f}")
    st.write(f"Perímetro: {perimetro:.2f}")
else:
    st.write("Por favor, introduce un valor de radio mayor a 0.")
