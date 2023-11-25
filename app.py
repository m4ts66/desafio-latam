import streamlit as st
from endpoints import code_gpt

# Configuración de la página
st.set_page_config(page_title="EmprendeBot", page_icon=":rocket:")

# Título principal
st.title("EmprendeBot")

# Formulario para la descripción de la empresa
emprendimiento_descripcion = st.text_area("Descripción del emprendimiento", "Escribe aquí...")

# Botón para enviar el formulario
if st.button("Enviar"):
    # Almacenar la descripción de la empresa en una variable de sesión
    st.session_state.emprendimiento_descripcion = emprendimiento_descripcion

# Verificar si la descripción de la empresa se ha ingresado antes de mostrar las pestañas
if "emprendimiento_descripcion" not in st.session_state or not st.session_state.emprendimiento_descripcion:
    st.warning("Por favor, ingresa una descripción de la empresa antes de continuar.")
else:
    # Barra lateral con pestañas
    selected_tab = st.sidebar.radio("Selecciona una pestaña", ["Orientación inicial", "Legal y financiera", "Desarrollo de producto"])

    # Contenido de la pestaña seleccionada
    if selected_tab == "Orientación inicial":
        st.header("Orientación inicial")
        mensaje = f"Necesito todo lo relacionado para realizar el inicio de mi emprendimiento, te dejo la descripción de este: {emprendimiento_descripcion}"
        agent_init = "06901da6-6dc2-4833-bad6-e7d5fd9712ab"
        init_info = code_gpt(mensaje, agent_init)
        st.write(init_info)

    elif selected_tab == "Legal y financiera":
        st.header("Legal y financiera")
        # Ejemplo de uso
        mensaje = f"Necesito toda la ayuda legal y financiera para implementar mi emprendimiento, te dejo la descripción de este: {emprendimiento_descripcion}"
        agent_legal = "db0091cc-fedd-4708-9396-98b9c1f081d2"
        legal_info = code_gpt(mensaje, agent_legal)
        st.write(legal_info)

    elif selected_tab == "Desarrollo de producto":
        st.header("Desarrollo de producto")
        mensaje = f"Necesito toda la ayuda para el desarrollo de los productos de mi emprendimiento, te dejo la descripción de este: {emprendimiento_descripcion}"
        agent_product = "3456f30c-ca7c-4d5e-bb19-cf8fcd4ff281"
        product_info = code_gpt(mensaje, agent_product)
        st.write(product_info)
