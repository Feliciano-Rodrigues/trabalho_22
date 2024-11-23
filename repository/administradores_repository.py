from entity.administradores import Administrador
from db import db

class AdministradoresRepository:
    def salvar(self, administrador):
        db.session.add(administrador)
        db.session.commit()
        return administrador.to_dict()

    def listar_todos(self):
        administradores = Administrador.query.all()
        return [administrador for administrador in administradores]

    def buscar_por_id(self, id):
        administrador = Administrador.query.get(id)
        return administrador if administrador else None

    def atualizar(self, administradores):
        db.session.add(administradores)
        db.session.commit()
        return administradores.to_dict()

    def deletar(self, administrador):
        db.session.delete(administrador)
        db.session.commit()
        return administrador.to_dict()
