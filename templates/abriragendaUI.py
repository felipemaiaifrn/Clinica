import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class AbrirAgendaUI:
  def main():
    st.header("Abrir Agenda do Dia")
    AbrirAgendaUI.abrir_agenda()
  
  def abrir_agenda():
    data = st.text_input("Informe a data no formato *dd/mm/aaaa*")
    hinicio = st.text_input("Informe o horário inicial no formato *HH\:MM*")
    hfim = st.text_input("Informe o horário final no formato *HH\:MM*")
    intervalo = st.text_input("Informe o intervalo entre os horários (min)")
    if st.button("Inserir Horários"):
      try:
        View.consulta_abrir_agenda(data, hinicio, hfim, int(intervalo))
        st.success("Horário(s) inserido(s) com sucesso")
        time.sleep(2)
        st.rerun()
      except TypeError as erro:
        st.error(erro)
      except ValueError:
        st.error('Data inválida!')