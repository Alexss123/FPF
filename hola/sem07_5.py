import streamlit as st 
#Funcion principal para verificar automoviles
def verificar_automviles():
    st.title("Centro de verificacion de automoviles")

    #Lista para almacenar los puntos contaminantes
    if "puntos_contaminantes" not in st.session_state
    st.session_state.puntos_contaminantes = []

#Imput para los puntos contaminantes del automvil
puntos = st.number_imput

