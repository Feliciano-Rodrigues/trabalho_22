from repository.leito_repository import LeitoRepository
from entity.leito import Leito

class LeitoService:
    def __init__(self):
        self.repository = LeitoRepository()

    def criar_leito(self, data):
        leito = Leito(
            setor=data['setor'],
            tipo=data['tipo'],
            ocupado=data.get('ocupado', False),
            id_veterinario_responsavel=data.get('id_veterinario_responsavel')
        )
        return self.repository.salvar(leito)

    def listar_leitos(self):
        return self.repository.listar_todos()

    def buscar_leito(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_leito(self, id, data):
        leito = Leito.query.get(id)
        if not leito:
            return None
        if 'setor' in data:
            leito.setor = data['setor']
        if 'tipo' in data:
            leito.tipo = data['tipo']
        if 'ocupado' in data:
            leito.ocupado = data['ocupado']
        if 'id_veterinario_responsavel' in data:
            leito.id_veterinario_responsavel = data['id_veterinario_responsavel']
        return self.repository.atualizar(leito)

    def deletar_leito(self, id):
        leito = Leito.query.get(id)
        if leito:
            self.repository.deletar(leito)
            return True
        return False
