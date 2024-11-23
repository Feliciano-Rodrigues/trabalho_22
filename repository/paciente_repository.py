from entity.paciente import Paciente
from db import db

class PacienteRepository:
    def salvar(self, paciente):
        db.session.add(paciente)
        db.session.commit()
        return paciente.to_dict()

    def listar_todos(self):
        pacientes = Paciente.query.all()
        return [paciente.to_dict() for paciente in pacientes]

    def buscar_por_id(self, id):
        paciente = Paciente.query.get(id)
        return paciente.to_dict() if paciente else None

    def atualizar(self, paciente):
        db.session.add(paciente)
        db.session.commit()
        return paciente.to_dict()

    def deletar(self, paciente):
        db.session.delete(paciente)
        db.session.commit()
        return paciente.to_dict()
