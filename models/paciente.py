import json

class Paciente:

    def __init__(self, id, nome, cpf, fone, senha):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_cpf(self, cpf): self.__cpf = cpf
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha

    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__fone}"
    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__cpf == x.__cpf and self.__fone == x.__fone and self.__senha == x.__senha:
            return True
        return False
   
class NPaciente:
    __pacientes = []
   
    @classmethod
    def inserir(cls, x):
        NPaciente.abrir()
        id = 0
        for paciente in cls.__pacientes:
            if paciente.get_id() > id: id = paciente.get_id()
        x.set_id(id+1)
        for c in cls.__pacientes:
            if c.get_cpf() == x.get_cpf():
                return False
        cls.__pacientes.append(x)
        NPaciente.salvar()

    @classmethod
    def listar(cls):
        NPaciente.abrir()
        return cls.__pacientes

    @classmethod
    def listar_id(cls, id):
        NPaciente.abrir()
        for paciente in cls.__pacientes:
            if paciente.get_id() == id:
                return paciente
        return None    

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        paciente = cls.listar_id(obj.get_id())
        if paciente is not None:
            paciente.set_nome(obj.get_nome)
            paciente.set_cpf(obj.get_cpf)
            paciente.set_fone(obj.get_fone)
            paciente.set_senha(obj.get_senha)
            NPaciente.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        p = cls.listar_id(obj.get_id())
        if p is not None:
            cls.__pacientes.remove(p)
            NPaciente.salvar()

    @classmethod
    def ver_cpf(cls, cpf):
        for paciente in cls.__pacientes:
            if cpf == paciente.get_cpf():
                return False
        return True

    @classmethod
    def abrir(cls):
        cls.__pacientes = []
        try:
            with open("pacientes.json", mode="r") as arquivo:
                pacientes_json = json.load(arquivo)
                for obj in pacientes_json:
                    p = Paciente(obj["_Paciente__id"], obj["_Paciente__nome"], obj["_Paciente__cpf"], obj["_Paciente__fone"], obj["_Paciente__senha"])
                    cls.__pacientes.append(p)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('pacientes.json', mode='w') as arquivo:
            json.dump(cls.__pacientes, arquivo, default=vars, indent=2)