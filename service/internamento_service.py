from repository.internamento_repository import InternamentoRepository
from entity.internamento import Internamento

class InternamentoService:
    def __init__(self):
        self.repository = InternamentoRepository()

    def criar_internamento(self, data):
        internamento = Internamento(
            id_paciente=data['id_paciente'],
            id_leito=data['id_leito'],
            data_inicio=data['data_inicio'],
            data_fim=data.get('data_fim'),
            motivo=data['motivo']
        )
        return self.repository.salvar(internamento)

    def listar_internamentos(self):
        return self.repository.listar_todos()

    def buscar_internamento(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_internamento(self, id, data):
        internamento = Internamento.query.get(id)
        if not internamento:
            return None
        if 'id_paciente' in data:
            internamento.id_paciente = data['id_paciente']
        if 'id_leito' in data:
            internamento.id_leito = data['id_leito']
        if 'data_inicio' in data:
            internamento.data_inicio = data['data_inicio']
        if 'data_fim' in data:
            internamento.data_fim = data['data_fim']
        if 'motivo' in data:
            internamento.motivo = data['motivo']
        return self.repository.atualizar(internamento)

    def deletar_internamento(self, id):
        internamento = Internamento.query.get(id)
        if internamento:
            self.repository.deletar(internamento)
            return True
        return False
