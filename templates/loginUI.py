import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header('Login')
        LoginUI.entrar()

    def entrar():
        cpf = st.text_input("Informe o CPF", key=1)
        senha = st.text_input("Informe a senha", key=2)
        if st.button("Login"):
          paciente = View.paciente_login(cpf, senha) 
          if paciente is not None:
            st.success("Login realizado com sucesso")
            st.success("Bem-vindo(a), " + paciente.get_nome())
            st.session_state["paciente_id"] = paciente.get_id()
            st.session_state["paciente_nome"] = paciente.get_nome()
          else:
            st.error("Usuário ou senha inválido(s)")
          time.sleep(2)
          st.rerun()   