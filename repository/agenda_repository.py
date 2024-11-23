from entity.agenda import Agenda
from db import db

class AgendaRepository:
    def criar_agenda(self, agenda):
        db.session.add(agenda)
        db.session.commit()
        return agenda  # Retorna o objeto Agenda criado

    def listar_agendas(self):
        return Agenda.query.all()  # Retorna uma lista de objetos Agenda

    def buscar_agenda(self, id):
        return Agenda.query.get(id)  # Retorna o objeto Agenda ou None

    def atualizar_agenda(self, agenda):
        db.session.add(agenda)
        db.session.commit()
        return agenda  # Retorna o objeto atualizado

    def deletar_agenda(self, agenda):
        db.session.delete(agenda)
        db.session.commit()
