from entity.consulta import Consulta
from db import db

class ConsultaRepository:
    def salvar(self, consulta):
        db.session.add(consulta)
        db.session.commit()
        return consulta.to_dict()

    def listar_todas(self):
        consultas = Consulta.query.all()
        return [consulta.to_dict() for consulta in consultas]

    def buscar_por_id(self, id):
        consulta = Consulta.query.get(id)
        return consulta.to_dict() if consulta else None

    def atualizar(self, consulta):
        db.session.add(consulta)
        db.session.commit()
        return consulta.to_dict()

    def deletar(self, consulta):
        db.session.delete(consulta)
        db.session.commit()
        return consulta.to_dict()

