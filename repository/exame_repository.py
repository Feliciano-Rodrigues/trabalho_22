from db import db
from entity.exame import Exame


class ExameRepository:
    def listar_exames(self):
        return Exame.query.all()

    def buscar_exame(self, id):
        return Exame.query.get(id)

    def criar_exame(self, exame: Exame):
        try:
            db.session.add(exame)
            db.session.commit()
            return exame
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar exame: {str(e)}")

    def atualizar_exame(self, exame: Exame):
        try:
            db.session.commit()
            return exame
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao atualizar exame: {str(e)}")

    def deletar_exame(self, id):
        exame = self.buscar_exame(id)
        if exame:
            try:
                db.session.delete(exame)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Erro ao deletar exame: {str(e)}")
        return False
