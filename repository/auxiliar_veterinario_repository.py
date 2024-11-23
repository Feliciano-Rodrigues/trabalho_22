from entity.auxiliar_veterinario import AuxiliarVeterinario
from db import db

class AuxiliarVeterinarioRepository:
    def salvar(self, auxiliar_veterinario):
        db.session.add(auxiliar_veterinario)
        db.session.commit()
        return auxiliar_veterinario.to_dict()

    def listar_todos(self):
        auxiliares = AuxiliarVeterinario.query.all()
        return [auxiliar.to_dict() for auxiliar in auxiliares]

    def buscar_por_id(self, id):
        auxiliar = AuxiliarVeterinario.query.get(id)
        return auxiliar.to_dict() if auxiliar else None

    def atualizar(self, auxiliar_veterinario):
        db.session.add(auxiliar_veterinario)
        db.session.commit()
        return auxiliar_veterinario.to_dict()

    def deletar(self, auxiliar_veterinario):
        db.session.delete(auxiliar_veterinario)
        db.session.commit()
        return auxiliar_veterinario.to_dict()
