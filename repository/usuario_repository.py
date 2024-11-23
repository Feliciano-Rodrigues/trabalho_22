from entity.usuario import Usuario
from db import db

class UsuarioRepository:
    def salvar(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_dict()

    def listar_todos(self):
        usuarios = Usuario.query.all()
        return [usuario.to_dict() for usuario in usuarios]

    def buscar_por_id(self, id):
        usuario = Usuario.query.get(id)
        return usuario.to_dict() if usuario else None

    def atualizar(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_dict()

    def deletar(self, usuario):
        db.session.delete(usuario)
        db.session.commit()
        return usuario.to_dict()
