from repository.auxiliar_veterinario_repository import AuxiliarVeterinarioRepository
from entity.auxiliar_veterinario import AuxiliarVeterinario

class AuxiliarVeterinarioService:
    def __init__(self):
        self.repository = AuxiliarVeterinarioRepository()

    def criar_auxiliar_veterinario(self, data):
        auxiliar_veterinario = AuxiliarVeterinario(
            nome=data['nome'],
            telefone=data.get('telefone'),
            email=data.get('email'),
            endereco=data.get('endereco')
        )
        return self.repository.salvar(auxiliar_veterinario)

    def listar_auxiliares(self):
        return self.repository.listar_todos()

    def buscar_auxiliar(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_auxiliar(self, id, data):
        auxiliar = AuxiliarVeterinario.query.get(id)
        if not auxiliar:
            return None
        if 'nome' in data:
            auxiliar.nome = data['nome']
        if 'telefone' in data:
            auxiliar.telefone = data['telefone']
        if 'email' in data:
            auxiliar.email = data['email']
        if 'endereco' in data:
            auxiliar.endereco = data['endereco']
        return self.repository.atualizar(auxiliar)

    def deletar_auxiliar(self, id):
        auxiliar = AuxiliarVeterinario.query.get(id)
        if auxiliar:
            self.repository.deletar(auxiliar)
            return True
        return False
