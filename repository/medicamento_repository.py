from entity.medicamento import Medicamento
from db import db

class MedicamentoRepository:
    def salvar(self, medicamento):
        db.session.add(medicamento)
        db.session.commit()
        return medicamento.to_dict()

    def listar_todos(self):
        medicamentos = Medicamento.query.all()
        return [medicamento.to_dict() for medicamento in medicamentos]

    def buscar_por_id(self, id):
        medicamento = Medicamento.query.get(id)
        return medicamento.to_dict() if medicamento else None

    def atualizar(self, medicamento):
        db.session.add(medicamento)
        db.session.commit()
        return medicamento.to_dict()

    def deletar(self, medicamento):
        db.session.delete(medicamento)
        db.session.commit()
        return medicamento.to_dict()
