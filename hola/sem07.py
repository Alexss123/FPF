import streamlit as st 
def mostrar_menu():
    st.title("BRIANA se baña?")
    st.write("Selecciona la opcion correcta")
    
    menu = ["Obviamente que no", "Eso nunca pasara", "Las dos anteriores", "Que se bañe de una vez"]
    seleccion = ""
    
    seleccion = st.radio("Menú", menu)
    
    if seleccion == "Obviamente que no":
        st.write("Seleccionaste: Que no")
    elif seleccion == "Eso nunca pasara":
        st.write("Seleccionaste: ojala lo haga pronto")
    elif seleccion == "Las dos anteriores":
        st.write("Seleccionaste: buena eleccion")
    elif seleccion == "Que se bañe de una vez":
        st.write("¡Oremos por eso!")

if __name__ == "__main__":
    mostrar_menu()