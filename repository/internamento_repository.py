from entity.internamento import Internamento
from db import db

class InternamentoRepository:
    def salvar(self, internamento):
        db.session.add(internamento)
        db.session.commit()
        return internamento.to_dict()

    def listar_todos(self):
        internamentos = Internamento.query.all()
        return [internamento.to_dict() for internamento in internamentos]

    def buscar_por_id(self, id):
        internamento = Internamento.query.get(id)
        return internamento.to_dict() if internamento else None

    def atualizar(self, internamento):
        db.session.add(internamento)
        db.session.commit()
        return internamento.to_dict()

    def deletar(self, internamento):
        db.session.delete(internamento)
        db.session.commit()
        return internamento.to_dict()
