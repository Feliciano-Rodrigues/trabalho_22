from repository.usuario_repository import UsuarioRepository
from entity.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def criar_usuario(self, data):
        usuario = Usuario(nome=data['nome'], email=data['email'])
        return self.repository.salvar(usuario)

    def listar_usuarios(self):
        return self.repository.listar_todos()

    def buscar_usuario(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_usuario(self, id, data):
        usuario = Usuario.query.get(id)
        if not usuario:
            return None
        if 'nome' in data:
            usuario.nome = data['nome']
        if 'email' in data:
            usuario.email = data['email']
        return self.repository.atualizar(usuario)

    def deletar_usuario(self, id):
        usuario = Usuario.query.get(id)
        if usuario:
            self.repository.deletar(usuario)
            return True
        return False
