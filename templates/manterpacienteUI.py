import streamlit as st
import pandas as pd
from views import View
import time

class ManterPacienteUI:
  def main():
    st.header("Cadastro de Pacientes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterPacienteUI.listar()
    with tab2: ManterPacienteUI.inserir()
    with tab3: ManterPacienteUI.atualizar()
    with tab4: ManterPacienteUI.excluir()

  def listar():
    pacientes = View.paciente_listar()
    if len(pacientes) == 0:
      st.write("Nenhum paciente cadastrado")
    else:
      dic = []
      for obj in pacientes: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    cpf = st.text_input("Informe o CPF")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      try:
        View.paciente_inserir(nome, cpf, fone, senha)
        st.success("Paciente inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as erro:
        st.error(erro)


  def atualizar():
    pacientes = View.paciente_listar()
    if len(pacientes) == 0:
      st.write("Nenhum paciente cadastrado")
    else:
      op = st.selectbox("Atualização de Pacientes", pacientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      cpf = st.text_input("Informe o novo CPF", op.get_cpf())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha")
      if st.button("Atualizar"):
        try:
          id = op.get_id()
          View.paciente_atualizar(id, nome, cpf, fone, senha)
          st.success("Paciente atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except ValueError as erro:
          st.error(erro)

  def excluir():
    pacientes = View.paciente_listar()
    if len(pacientes) == 0:
      st.write("Nenhum paciente cadastrado")
    else:
      op = st.selectbox("Exclusão de Pacientes", pacientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.paciente_excluir(id)
        st.success("Paciente excluído com sucesso")
        time.sleep(2)
        st.rerun()