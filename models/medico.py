import json

class Medico:
  def __init__(self, id, nome, crm, senha):
    self.__id = id
    self.__nome = nome
    self.__crm = crm
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_crm(self): return self.__crm
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_crm(self, crm): self.__crm = crm
  def set_senha(self, senha): self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__crm == x.__crm and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__crm} - {self.__senha}"


class NServico:
  __medicos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__medicos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__medicos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__medicos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__medicos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_crm(obj.get_crm())
      aux.set_senha(obj.get_senha())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__medicos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__medicos = []
    try:
      with open("medicos.json", mode="r") as arquivo:
        medicos_json = json.load(arquivo)
        for obj in medicos_json:
          aux = Medico(obj["_Medico__id"], obj["_Medico__nome"], obj["_Medico__crm"], obj["_Medico__senha"])
          cls.__medicos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("medicos.json", mode="w") as arquivo:
      json.dump(cls.__medicos, arquivo, default=vars, indent=2)