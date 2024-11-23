from repository.consulta_repository import ConsultaRepository
from entity.consulta import Consulta

class ConsultaService:
    def __init__(self):
        self.repository = ConsultaRepository()

    def criar_consulta(self, data):
        consulta = Consulta(
            id_paciente=data['id_paciente'],
            id_veterinario=data['id_veterinario'],
            data_consulta=data['data_consulta'],
            descricao=data.get('descricao'),
        )
        return self.repository.salvar(consulta)

    def listar_consultas(self):
        return self.repository.listar_todas()

    def buscar_consulta(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_consulta(self, id, data):
        consulta = Consulta.query.get(id)
        if not consulta:
            return None
        if 'id_paciente' in data:
            consulta.id_paciente = data['id_paciente']
        if 'id_veterinario' in data:
            consulta.id_veterinario = data['id_veterinario']
        if 'data_consulta' in data:
            consulta.data_consulta = data['data_consulta']
        if 'descricao' in data:
            consulta.descricao = data['descricao']
        return self.repository.atualizar(consulta)

    def deletar_consulta(self, id):
        consulta = Consulta.query.get(id)
        if consulta:
            self.repository.deletar(consulta)
            return True
        return False
