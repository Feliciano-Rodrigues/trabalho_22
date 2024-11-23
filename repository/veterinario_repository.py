from entity.veterinario import Veterinario
from db import db

class VeterinarioRepository:
    def salvar(self, veterinario):
        db.session.add(veterinario)
        db.session.commit()
        return veterinario.to_dict()

    def listar_todos(self):
        veterinarios = Veterinario.query.all()
        return [veterinario.to_dict() for veterinario in veterinarios]

    def buscar_por_id(self, id):
        veterinario = Veterinario.query.get(id)
        return veterinario.to_dict() if veterinario else None

    def atualizar(self, veterinario):
        db.session.add(veterinario)
        db.session.commit()
        return veterinario.to_dict()

    def deletar(self, veterinario):
        db.session.delete(veterinario)
        db.session.commit()
        return veterinario.to_dict()
