from db import db
from entity.leito import Leito

class LeitoRepository:
    def salvar(self, leito):
        db.session.add(leito)
        db.session.commit()
        return leito.to_dict()

    def listar_todos(self):
        leitos = Leito.query.all()
        return [leito.to_dict() for leito in leitos]

    def buscar_por_id(self, id):
        leito = Leito.query.get(id)
        return leito.to_dict() if leito else None

    def atualizar(self, leito):
        db.session.add(leito)
        db.session.commit()
        return leito.to_dict()

    def deletar(self, leito):
        db.session.delete(leito)
        db.session.commit()
