from models.paciente import Paciente, NPaciente
from models.medico import Medico, NMedico
from models.consulta import Consulta, NConsulta
import datetime

class View:
    
    def paciente_inserir(nome, cpf, fone, senha):
        if nome == '' or cpf == '' or fone == '' or senha == '': raise ValueError('Preencha os valores vazios!')
        if NPaciente.ver_cpf(cpf) == False: raise ValueError('CPF já cadastrado!')
        paciente = Paciente(0, nome, cpf, fone, senha)
        NPaciente.inserir(paciente)

    def paciente_listar():
        return NPaciente.listar()
  
    def paciente_listar_id(id):
        return NPaciente.listar_id(id)

    def paciente_atualizar(id, nome, cpf, fone, senha):
        if nome == '' or cpf == '' or fone == '' or senha == '': raise ValueError('Preencha os valores vazios!')
        if NPaciente.ver_cpf(cpf) == False: raise ValueError('CPF já cadastrado!')
        paciente = Paciente(id, nome, cpf, fone, senha)
        NPaciente.atualizar(paciente)
    
    def paciente_excluir(id):
        paciente = Paciente(id, "", "", "", "")
        NPaciente.excluir(paciente)    

    def paciente_login(cpf, senha):
        for paciente in View.paciente_listar():
            if paciente.get_cpf() == cpf and paciente.get_senha() == senha:
                return paciente
        return None



    def paciente_admin():
        for paciente in View.paciente_listar():
            if paciente.get_cpf() == "admin": return
        View.paciente_inserir("admin", "admin", "0000", "admin")

    def medico_listar():
        return NMedico.listar()

    def medico_listar_id(id):
        return NMedico.listar_id(id)

    def medico_inserir(nome, crm, senha):
        if nome == '' or crm == '' or senha == '': raise ValueError('Preencha os valores vazios!')
        NMedico.inserir(Medico(0, nome, crm, senha))

    def medico_atualizar(id, nome, crm, senha):
        NMedico.atualizar(Medico(id, nome, crm, senha))

    def medico_excluir(id):
        NMedico.excluir(Medico(id, "", "", ""))



    def consulta_listar():
        return NConsulta.listar()

    def consulta_listarhoje():
        r = []
        hoje = datetime.datetime.today().date()
        for horario in View.consulta_listar():
            if horario.get_confirmado() == False and horario.get_data().date() == hoje:
                r.append(horario)
        return r    

    def consulta_inserir(data, confirmado, id_paciente, id_medico):
        NConsulta.inserir(Consulta(0, data, confirmado, id_paciente, id_medico))

    def consulta_atualizar(id, data, confirmado, id_paciente, id_medico):
        NConsulta.atualizar(Consulta(id, data, confirmado, id_paciente, id_medico))

    def consulta_excluir(id):
        NConsulta.excluir(Consulta(id, "", "", 0, 0))

    def consultas_da_semana():
        lista = []
        hoje = datetime.datetime.today().date()
        setimo_dia = hoje + datetime.timedelta(days=7)
        for consulta in View.consulta_listar():
            if  hoje <= consulta.get_data().date() <= setimo_dia and consulta.get_confirmado() == False and consulta.get_id_paciente() == 0:
                lista.append(consulta)
        return lista
    
    def agendar_horario(id, id_paciente, id_medico):
        for consulta in View.consulta_listar():
            if consulta.get_id() == id:
                NConsulta.atualizar(Consulta(consulta.get_id(), consulta.get_data(), False, id_paciente, id_medico))

    def minhas_consultas(id , dataini_str, datafin_str):
        dataini = datetime.datetime.strptime(dataini_str, '%d/%m/%Y')        
        datafin = datetime.datetime.strptime(datafin_str, '%d/%m/%Y')        

        lista = []
        for consulta in View.consulta_listar():
            if consulta.get_id_paciente() == id and dataini.date() <= consulta.get_data().date() <= datafin.date():
                lista.append(consulta)
        return lista
    
    def consulta_confirmar(id):
        for consulta in View.consulta_listar():
            if id == consulta.get_id():
                NConsulta.atualizar(Consulta(consulta.get_id(), consulta.get_data(), True, consulta.get_id_paciente(), consulta.get_id_medico()))
    
    def consulta_abrir_agenda(data, hinicio, hfim, intervalo):
        data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
        data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
        delta = datetime.timedelta(minutes = intervalo) 
        aux = data_inicio

        if data_inicio < datetime.datetime.today():
            raise TypeError('A data não pode ter passado!')
        if intervalo <= 0:
            raise TypeError('O intervalo deve ser positivo!')
    
        while aux <= data_fim :
            NConsulta.inserir(Consulta(0, aux, "", False, 0, 0))
            aux = aux + delta



    def editar_perfil_paciente(id, nome, cpf, fone, senha):
        NPaciente.atualizar(Paciente(id, nome, cpf, fone, senha))

    def editar_perfil_medico(id, nome, crm, senha):
        NMedico.atualizar(Medico(id, nome, crm, senha))