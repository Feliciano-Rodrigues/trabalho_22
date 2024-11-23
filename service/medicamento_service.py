from repository.medicamento_repository import MedicamentoRepository
from entity.medicamento import Medicamento

class MedicamentoService:
    def __init__(self):
        self.repository = MedicamentoRepository()

    def criar_medicamento(self, data):
        medicamento = Medicamento(
            nome=data['nome'],
            descricao=data.get('descricao'),
            quantidade=data['quantidade'],
            unidade_medida=data['unidade_medida']
        )
        return self.repository.salvar(medicamento)

    def listar_medicamentos(self):
        return self.repository.listar_todos()

    def buscar_medicamento(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_medicamento(self, id, data):
        medicamento = Medicamento.query.get(id)
        if not medicamento:
            return None
        if 'nome' in data:
            medicamento.nome = data['nome']
        if 'descricao' in data:
            medicamento.descricao = data['descricao']
        if 'quantidade' in data:
            medicamento.quantidade = data['quantidade']
        if 'unidade_medida' in data:
            medicamento.unidade_medida = data['unidade_medida']
        return self.repository.atualizar(medicamento)

    def deletar_medicamento(self, id):
        medicamento = Medicamento.query.get(id)
        if medicamento:
            self.repository.deletar(medicamento)
            return True
        return False
