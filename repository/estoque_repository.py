from db import db
from entity.estoque import Estoque

class EstoqueRepository:
    def listar_estoques(self):
        return Estoque.query.all()

    def buscar_estoque(self, id):
        return Estoque.query.get(id)

    def criar_estoque(self, estoque: Estoque):
        try:
            db.session.add(estoque)
            db.session.commit()
            return estoque
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar estoque: {str(e)}")

    def atualizar_estoque(self, estoque: Estoque):
        try:
            db.session.commit()
            return estoque
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao atualizar estoque: {str(e)}")

    def deletar_estoque(self, id):
        estoque = self.buscar_estoque(id)
        if estoque:
            try:
                db.session.delete(estoque)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Erro ao deletar estoque: {str(e)}")
        return False
