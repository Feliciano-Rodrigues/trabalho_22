from datetime import datetime
from repository.estoque_repository import EstoqueRepository
from entity.estoque import Estoque

class EstoqueService:
    def __init__(self):
        self.estoque_repo = EstoqueRepository()

    def listar_estoques(self):
        return [estoque.to_dict() for estoque in self.estoque_repo.listar_estoques()]

    def buscar_estoque(self, id):
        estoque = self.estoque_repo.buscar_estoque(id)
        if estoque:
            return estoque.to_dict()
        return None

    def criar_estoque(self, data):
        try:
            estoque = Estoque(
                nome_produto=data['nome_produto'],
                quantidade=data['quantidade'],
                preco_unitario=data['preco_unitario'],
                data_entrada=datetime.strptime(data['data_entrada'], '%Y-%m-%d').date(),
                data_validade=datetime.strptime(data['data_validade'], '%Y-%m-%d').date() if 'data_validade' in data else None
            )
            return self.estoque_repo.criar_estoque(estoque).to_dict()
        except Exception as e:
            raise ValueError(f"Erro ao criar estoque: {str(e)}")

    def atualizar_estoque(self, id, data):
        estoque = self.estoque_repo.buscar_estoque(id)
        if not estoque:
            return None

        estoque.nome_produto = data.get('nome_produto', estoque.nome_produto)
        estoque.quantidade = data.get('quantidade', estoque.quantidade)
        estoque.preco_unitario = data.get('preco_unitario', estoque.preco_unitario)
        estoque.data_entrada = datetime.strptime(data.get('data_entrada', str(estoque.data_entrada)), '%Y-%m-%d').date()
        estoque.data_validade = datetime.strptime(data.get('data_validade', str(estoque.data_validade)), '%Y-%m-%d').date() if 'data_validade' in data else estoque.data_validade

        return self.estoque_repo.atualizar_estoque(estoque).to_dict()

    def deletar_estoque(self, id):
        estoque = self.estoque_repo.buscar_estoque(id)
        if not estoque:
            return False
        return self.estoque_repo.deletar_estoque(id)
