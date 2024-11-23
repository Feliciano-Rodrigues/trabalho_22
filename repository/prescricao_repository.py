from entity.prescricao import Prescricao
from db import db

class PrescricaoRepository:
    def salvar(self, prescricao):
        db.session.add(prescricao)
        db.session.commit()
        return prescricao.to_dict()

    def listar_todas(self):
        prescricoes = Prescricao.query.all()
        return [prescricao.to_dict() for prescricao in prescricoes]

    def buscar_por_id(self, id):
        prescricao = Prescricao.query.get(id)
        return prescricao.to_dict() if prescricao else None

    def atualizar(self, prescricao):
        db.session.add(prescricao)
        db.session.commit()
        return prescricao.to_dict()

    def deletar(self, prescricao):
        db.session.delete(prescricao)
        db.session.commit()
        return prescricao.to_dict()
