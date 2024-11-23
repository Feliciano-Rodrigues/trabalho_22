from entity.cirurgia import Cirurgia
from db import db

class CirurgiaRepository:
    def criar_cirurgia(self, cirurgia):
        db.session.add(cirurgia)
        db.session.commit()
        return cirurgia  # Retorna o objeto Cirurgia criado

    def listar_cirurgias(self):
        return Cirurgia.query.all()  # Retorna uma lista de objetos Cirurgia

    def buscar_cirurgia(self, id):
        return Cirurgia.query.get(id)  # Retorna o objeto Cirurgia ou None

    def atualizar_cirurgia(self, cirurgia):
        db.session.add(cirurgia)
        db.session.commit()
        return cirurgia  # Retorna o objeto atualizado

    def deletar_cirurgia(self, cirurgia):
        db.session.delete(cirurgia)
        db.session.commit()
