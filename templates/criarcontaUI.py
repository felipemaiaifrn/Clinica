import streamlit as st
from views import View
import time

class CriarContaUI:
  def main():
    st.header("Criar Conta na Clínica")
    CriarContaUI.inserir()

  def inserir():
    nome = st.text_input("Informe o nome")
    cpf = st.text_input("Informe o CPF")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      View.paciente_inserir(nome, cpf, fone, senha)
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()