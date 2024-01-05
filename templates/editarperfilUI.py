import streamlit as st
from views import View
import time

class EditarPerfilUI:
    def main():
        st.header('Editar Perfil')
        EditarPerfilUI.editar()

    def editar():
        id = st.session_state["paciente_id"]
        nome_admin = st.session_state["paciente_nome"]
        
        if nome_admin == 'admin':
            nome = nome_admin
            crm = st.text_input('Informe o novo CRM')
            senha = st.text_input('Informe a nova senha')
        else:
            nome = st.text_input('Informe o novo nome')
            cpf = st.text_input('Informe o novo CPF')
            telefone = st.text_input('Informe o novo telefone')
            senha = st.text_input('Informe a nova senha')

        if st.button('Editar'):
            if nome_admin == 'admin' :
                View.editar_perfil_medico(id, nome, crm, senha)
                st.success('Perfil editado com sucesso!')
                time.sleep(1)
                st.rerun()

            else:
                View.editar_perfil_paciente(id, nome, cpf, telefone, senha)
                st.success('Perfil editado com sucesso!')
                time.sleep(1)
                st.rerun()