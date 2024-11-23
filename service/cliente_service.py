from repository.cliente_repository import ClienteRepository
from entity.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def criar_cliente(self, data):
        cliente = Cliente(
            nome=data['nome'],
            endereco=data['endereco'],
            telefone=data['telefone'],
            contato_emergencial=data['contato_emergencial']
        )
        return self.repository.salvar(cliente)

    def listar_clientes(self):
        return self.repository.listar_todos()

    def buscar_cliente(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_cliente(self, id, data):
        cliente = Cliente.query.get(id)
        if not cliente:
            return None
        if 'nome' in data:
            cliente.nome = data['nome']
        if 'endereco' in data:
            cliente.endereco = data['endereco']
        if 'telefone' in data:
            cliente.telefone = data['telefone']
        if 'contato_emergencial' in data:
            cliente.contato_emergencial = data['contato_emergencial']
        return self.repository.atualizar(cliente)

    def deletar_cliente(self, id):
        cliente = Cliente.query.get(id)
        if cliente:
            self.repository.deletar(cliente)
            return True
        return False
