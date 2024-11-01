import streamlit as st

# Título de la aplicación
st.title("Verificación de Contraseña")

# Estado de sesión para controlar si el usuario ha ingresado la contraseña correcta
if 'acceso_concedido' not in st.session_state:
    st.session_state.acceso_concedido = False

# Formulario para ingresar la contraseña
if not st.session_state.acceso_concedido:
    with st.form("form_contraseña"):
        contraseña = st.text_input("Ingresa la contraseña:", type="password")
        submit = st.form_submit_button("Enviar")

        if submit:
            if contraseña == "asdasd":
                st.session_state.acceso_concedido = True
                st.success("Bienvenido")
            else:
                st.error("Contraseña incorrecta, inténtalo nuevamente.")
else:
    st.write("Ya tienes acceso. ¡Bienvenido!")
