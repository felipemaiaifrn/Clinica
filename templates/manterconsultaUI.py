import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class ManterConsultaUI:
  def main():
    st.header("Cadastro de Consultas")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterConsultaUI.listar()
    with tab2: ManterConsultaUI.inserir()
    with tab3: ManterConsultaUI.atualizar()
    with tab4: ManterConsultaUI.excluir()  

  def listar():
    consultas = View.consulta_listar()
    if len(consultas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      tabela = []
      
      for consulta in View.consulta_listar():
        id = consulta.get_id()
        data = consulta.get_data()
        desc = consulta.get_descricao()
        conf = consulta.get_confirmado()
        idPaciente = int(consulta.get_id_paciente())
        idMedico = int(st.session_state["paciente_id"])

        if idPaciente != 0 and idMedico != 0:
          for paciente in View.paciente_listar():
            if idPaciente == paciente.get_id(): idPaciente = paciente.get_nome()
            
          for medico in View.medico_listar():
            if idMedico == medico.get_id(): idMedico = medico.get_nome()

        tabela.append([id, data, desc, conf, idPaciente, idMedico])

      df = pd.DataFrame(tabela, columns=['Id', 'Data', 'Descrição', 'Confirmado', 'Paciente', 'Médico'])

      st.dataframe(df, use_container_width=True)

  def inserir():
    datastr = st.text_input("Informe a data no formato *dd/mm/aaaa HH\:MM*")
    desc = st.text_input("Descrição da consulta")
    pacientes = View.paciente_listar()
    paciente = st.selectbox("Selecione o paciente", pacientes)
    #medicos = View.medico_listar()
    #medico = st.selectbox("Selecione o médico", medicos)
    if st.button("Inserir"):
      try:
        data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        View.consulta_inserir(data, desc, False, paciente.get_id(), st.session_state["paciente_id"])
        st.success("Horário inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.error('Data inválida!')

  def atualizar():
    consultas = View.consulta_listar()
    if len(consultas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Atualização de horários", consultas)
      datastr = st.text_input("Informe a nova data no formato *dd/mm/aaaa HH\:MM*", op.get_data().strftime('%d/%m/%Y %H:%M'))
      desc = st.text_input("Informe a nova descrição da consulta")
      pacientes = View.paciente_listar()
      paciente_atual = View.paciente_listar_id(op.get_id_paciente())
      if paciente_atual is not None:
        paciente = st.selectbox("Selecione o novo paciente", pacientes, pacientes.index(paciente_atual))
      else:  
        paciente = st.selectbox("Selecione o novo paciente", pacientes)
      #medicos = View.medico_listar()
      #medico_atual = View.medico_listar_id(op.get_id_medico())
      #if medico_atual is not None:
      #  medico = st.selectbox("Selecione o novo médico", medicos, medicos.index(medico_atual))
      #else:
      #  medico = st.selectbox("Selecione o novo médico", medicos)
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
          View.consulta_atualizar(op.get_id(), data, desc, op.get_confirmado(), paciente.get_id(), st.session_state["paciente_id"])
          st.success("Horário atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except ValueError:
          st.error('Data inválida!')

  def excluir():
    consultas = View.consulta_listar()
    if len(consultas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Exclusão de horários", consultas)
      if st.button("Excluir"):
        View.consulta_excluir(op.get_id())
        st.success("Horário excluído com sucesso")
        time.sleep(2)
        st.rerun()