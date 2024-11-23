# repository/financeiro_repository.py
from db import db
from entity.financeiro import Financeiro

class FinanceiroRepository:
    def listar_financeiros(self):
        return Financeiro.query.all()

    def buscar_financeiro(self, id):
        return Financeiro.query.get(id)

    def criar_financeiro(self, financeiro):
        try:
            db.session.add(financeiro)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar financeiro: {str(e)}")

    def atualizar_financeiro(self, financeiro):
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao atualizar financeiro: {str(e)}")

    def deletar_financeiro(self, id):
        financeiro = Financeiro.query.get(id)
        if financeiro:
            try:
                db.session.delete(financeiro)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Erro ao deletar financeiro: {str(e)}")
        return False
