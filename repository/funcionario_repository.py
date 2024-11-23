from entity.funcionario import Funcionario
from db import db

class FuncionarioRepository:
    def salvar(self, funcionario):
        db.session.add(funcionario)
        db.session.commit()
        return funcionario.to_dict()

    def listar_todos(self):
        funcionarios = Funcionario.query.all()
        return [funcionario.to_dict() for funcionario in funcionarios]

    def buscar_por_id(self, id):
        funcionario = Funcionario.query.get(id)
        return funcionario.to_dict() if funcionario else None

    def atualizar(self, funcionario):
        db.session.add(funcionario)
        db.session.commit()
        return funcionario.to_dict()

    def deletar(self, funcionario):
        db.session.delete(funcionario)
        db.session.commit()
        return funcionario.to_dict()

    def buscar_por_cpf(self, cpf):
        funcionario = Funcionario.query.filter_by(cpf=cpf).first()
        return funcionario.to_dict() if funcionario else None
