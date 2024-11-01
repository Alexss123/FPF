import streamlit as st

# Título de la aplicación
st.title("Cálculo de Suma y Media de Números")

# Estado de sesión para almacenar números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Formulario para ingresar números
with st.form("input_form"):
    numero = st.number_input("Ingresa un número (0 para finalizar):", value=0, step=1)
    submit = st.form_submit_button("Añadir número")

    # Si se envía el formulario
    if submit:
        if numero != 0:
            st.session_state.numeros.append(numero)
            st.success(f"Número {numero} añadido a la lista.")
        else:
            st.warning("Has ingresado un 0, se calcularán la suma y la media de los números.")

# Si se ha ingresado un 0, calcular la suma y la media
if 0 in st.session_state.numeros:
    st.session_state.numeros.remove(0)  # Remueve el cero si se ingresó

    if len(st.session_state.numeros) > 0:
        suma = sum(st.session_state.numeros)
        media = suma / len(st.session_state.numeros)
        
        st.write("### Resultados:")
        st.write(f"Suma de los números ingresados: {suma}")
        st.write(f"Media de los números ingresados: {media:.2f}")
    else:
        st.write("No se han ingresado números distintos de cero.")

# Botón para reiniciar los datos
if st.button("Reiniciar"):
    st.session_state.numeros = []
    st.success("Los datos han sido reiniciados.")
