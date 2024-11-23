from repository.veterinario_repository import VeterinarioRepository
from entity.veterinario import Veterinario

class VeterinarioService:
    def __init__(self):
        self.repository = VeterinarioRepository()

    def criar_veterinario(self, data):
        veterinario = Veterinario(
            nome=data['nome'],
            crmv=data['crmv'],
            telefone=data.get('telefone'),
            email=data.get('email'),
            endereco=data.get('endereco')
        )
        return self.repository.salvar(veterinario)

    def listar_veterinarios(self):
        return self.repository.listar_todos()

    def buscar_veterinario(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_veterinario(self, id, data):
        veterinario = Veterinario.query.get(id)
        if not veterinario:
            return None
        if 'nome' in data:
            veterinario.nome = data['nome']
        if 'crmv' in data:
            veterinario.crmv = data['crmv']
        if 'telefone' in data:
            veterinario.telefone = data['telefone']
        if 'email' in data:
            veterinario.email = data['email']
        if 'endereco' in data:
            veterinario.endereco = data['endereco']
        return self.repository.atualizar(veterinario)

    def deletar_veterinario(self, id):
        veterinario = Veterinario.query.get(id)
        if veterinario:
            self.repository.deletar(veterinario)
            return True
        return False
