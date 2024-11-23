from repository.prescricao_repository import PrescricaoRepository
from entity.prescricao import Prescricao

class PrescricaoService:
    def __init__(self):
        self.repository = PrescricaoRepository()

    def criar_prescricao(self, data):
        prescricao = Prescricao(
            id_consulta=data['id_consulta'],
            medicamento=data['medicamento'],
            dosagem=data['dosagem'],
            frequencia=data['frequencia'],
            duracao=data['duracao'],
            observacoes=data.get('observacoes')
        )
        return self.repository.salvar(prescricao)

    def listar_prescricoes(self):
        return self.repository.listar_todas()

    def buscar_prescricao(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_prescricao(self, id, data):
        prescricao = Prescricao.query.get(id)
        if not prescricao:
            return None
        if 'medicamento' in data:
            prescricao.medicamento = data['medicamento']
        if 'dosagem' in data:
            prescricao.dosagem = data['dosagem']
        if 'frequencia' in data:
            prescricao.frequencia = data['frequencia']
        if 'duracao' in data:
            prescricao.duracao = data['duracao']
        if 'observacoes' in data:
            prescricao.observacoes = data['observacoes']
        return self.repository.atualizar(prescricao)

    def deletar_prescricao(self, id):
        prescricao = Prescricao.query.get(id)
        if prescricao:
            self.repository.deletar(prescricao)
            return True
        return False
