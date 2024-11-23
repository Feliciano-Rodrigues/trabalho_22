# service/financeiro_service.py
from repository.financeiro_repository import FinanceiroRepository
from datetime import datetime
from entity.financeiro import Financeiro

class FinanceiroService:
    def __init__(self):
        self.repository = FinanceiroRepository()

    def listar_financeiros(self):
        return self.repository.listar_financeiros()

    def buscar_financeiro(self, id):
        return self.repository.buscar_financeiro(id)

    def criar_financeiro(self, data):
        try:
            financeiro = Financeiro(
                tipo=data['tipo'],
                valor=data['valor'],
                data=datetime.strptime(data['data'], '%Y-%m-%dT%H:%M:%S'),
                descricao=data.get('descricao', None)
            )
            self.repository.criar_financeiro(financeiro)
            return financeiro
        except Exception as e:
            raise ValueError(f"Erro ao criar financeiro: {str(e)}")

    def atualizar_financeiro(self, id, data):
        financeiro = self.repository.buscar_financeiro(id)
        if not financeiro:
            return None

        financeiro.tipo = data.get('tipo', financeiro.tipo)
        financeiro.valor = data.get('valor', financeiro.valor)
        financeiro.data = datetime.strptime(data.get('data', financeiro.data.isoformat()), '%Y-%m-%dT%H:%M:%S')
        financeiro.descricao = data.get('descricao', financeiro.descricao)

        self.repository.atualizar_financeiro(financeiro)
        return financeiro

    def deletar_financeiro(self, id):
        return self.repository.deletar_financeiro(id)
