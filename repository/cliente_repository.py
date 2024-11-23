from entity.cliente import Cliente
from db import db

class ClienteRepository:
    def salvar(self, cliente):
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_dict()

    def listar_todos(self):
        clientes = Cliente.query.all()
        return [cliente.to_dict() for cliente in clientes]

    def buscar_por_id(self, id):
        cliente = Cliente.query.get(id)
        return cliente.to_dict() if cliente else None

    def atualizar(self, cliente):
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_dict()

    def deletar(self, cliente):
        db.session.delete(cliente)
        db.session.commit()
        return cliente.to_dict()
