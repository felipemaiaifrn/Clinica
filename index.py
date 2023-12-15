from templates.manterpacienteUI import ManterPacienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterconsultaUI import ManterConsultaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.confirmarconsultaUI import ConfirmarConsultaUI
from templates.loginUI import LoginUI
from templates.editarperfilUI import EditarPerfilUI
from templates.criarcontaUI import CriarContaUI
from templates.agendasemanaUI import AgendaSemanaUI
from templates.agendarconsultaUI import AgendarConsultaUI
from templates.minhasconsultasUI import MinhasConsultasUI

import streamlit as st

class IndexUI:
    def sidebar():
        op = st.sidebar.selectbox("Menu", ["Login", "Criar conta no Sistema", "Agenda da Semana", "Agendar Consulta", "Minhas Consultas", "Editar Perfil", "Manter Pacientes", "Manter Horários", "Manter Agenda", "Abrir Agenda do Dia", "Confirmar Consulta", "Editar Perfil"])
        if op == "Login": LoginUI.main()
        if op == "Criar conta no Sistema": CriarContaUI.main()
        if op == "Agenda da Semana": AgendaSemanaUI.main()
        if op == "Agendar Consulta": AgendarConsultaUI.main()
        if op == "Minhas Consultas": MinhasConsultasUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()
        if op == "Manter Pacientes": ManterPacienteUI.main()
        if op == "Manter Horários": ManterHorarioUI.main()
        if op == "Manter Consultas": ManterConsultaUI.main()
        if op == "Abrir Agenda da Semana": AbrirAgendaUI.main()
        if op == "Confirmar Consulta": ConfirmarConsultaUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()

    #def menu_visitante():
    #  op = st.sidebar.selectbox("Menu", ["Login", "Criar conta no Sistema"])
    #  if op == "Login": LoginUI.main()
    #  if op == "Criar conta no Sistema": CriarContaUI.main()
    #def menu_cliente():
    #  op = st.sidebar.selectbox("Menu", ["Agenda da Semana", "Agendar Consulta", "Minhas Consultas", "Editar Perfil"])
    #  if op == "Agenda da Semana": AgendaSemanaUI.main()
    #  if op == "Agendar Consulta": AgendarConsultaUI.main()
    #  if op == "Minhas Consultas": MinhasConsultasUI.main()
    #  if op == "Editar Perfil": EditarPerfilUI.main()
    #def menu_admin():
    #  op = st.sidebar.selectbox("Menu", ["Manter Pacientes", "Manter Horários", "Manter Agenda", "Abrir Agenda do Dia", "Confirmar Consulta", "Editar Perfil"])
    #  if op == "Manter Pacientes": ManterPacienteUI.main()
    #  if op == "Manter Horários": ManterHorarioUI.main()
    #  if op == "Manter Consultas": ManterConsultaUI.main()
    #  if op == "Abrir Agenda da Semana": AbrirAgendaUI.main()
    #  if op == "Confirmar Consulta": ConfirmarConsultaUI.main()
    #  if op == "Editar Perfil": EditarPerfilUI.main()
    #def logout():
    #  if st.sidebar.button('Logout'):
    #    del st.session_state["cliente_id"]
    #    del st.session_state["cliente_nome"]
    #    st.rerun()
    #def sidebar():
    #  if "cliente_id" not in st.session_state:
    #    IndexUI.menu_visitante()
    #  else:
    #      if st.session_state["cliente_nome"] != "admin":
    #        IndexUI.menu_cliente()
    #      else:
    #        IndexUI.menu_admin()
    #        
    #      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
    #      IndexUI.logout()
    def main():
      IndexUI.sidebar()



IndexUI.main()