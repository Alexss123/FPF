import streamlit as st 

#Funcion principal para verificar automoviles
def verificar_automviles():
    st.title("Centro de verificacion de automoviles")

    #Lista para almacenar los puntos contaminantes
    if 'puntos_contaminantes' not in st.session_state:
        st.session_state.puntos_contaminantes = []

    #Imput para los puntos contaminantes del automvil
    puntos = st.number_input("Ingrese los puntos contaminantes del automovil", min_value=0.0, step=0.1 )

    #Boton para registrar el automovil
    if st.button("Registrar automovil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automvil registrado con {puntos} puntos contaminantes")

    #Mostrar los datos registrados hasta el momento
    if len(st.session_state.puntos_contaminantes) > 0 and st.button("Calcular resultados"):
        promedio = sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        # Mostrar los resultados
        st.write(f"Promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"El automóvil que menos contaminó tiene {menos_contaminacion}")
        st.write(f"El automóvil que más contaminó tiene {mas_contaminacion}")

    #Opción para reiniciar los datos
    if st.button("Reiniciar datos"):
        st.session_state.puntos_contaminantes = []
        st.success("Datos reiniciados correctamente")

#Ejecutar la función
if __name__ == "__main__":
    verificar_automoviles()