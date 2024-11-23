from repository.administradores_repository import AdministradoresRepository
from entity.administradores import Administrador  # Entidade

class AdministradoresService:
    def __init__(self):
        self.administrador_repo = AdministradoresRepository()

    def listar_administradores(self):
        # Utiliza o método listar_todos do repositório corretamente
        return self.administrador_repo.listar_todos()

    def buscar_administrador(self, id):
        # Busca por ID e retorna o dicionário ou None
        administrador = self.administrador_repo.buscar_por_id(id)
        return administrador if administrador else None

    def criar_administrador(self, data):
        try:
            # Cria uma nova instância de Administrador com os dados fornecidos
            administrador = Administrador(
                nome=data['nome'],
                email=data['email'],
                senha=data['senha']
            )
            # Salva o administrador no banco de dados
            return self.administrador_repo.salvar(administrador)
        except Exception as e:
            raise ValueError(f"Erro ao criar administrador: {str(e)}")

    def atualizar_administrador(self, id, data):
        # Busca o administrador existente
        administrador = self.administrador_repo.buscar_por_id(id)
        if not administrador:
            return None
        # Atualiza os campos do administrador com os dados fornecidos
        administrador.nome = data.get('nome', administrador.nome)
        administrador.email = data.get('email', administrador.email)
        administrador.senha = data.get('senha', administrador.senha)
        # Salva as alterações no banco de dados
        return self.administrador_repo.atualizar(administrador)

    def deletar_administrador(self, id):
        # Busca o administrador antes de deletar
        administrador = self.administrador_repo.buscar_por_id(id)
        if not administrador:
            return False
        # Deleta o administrador do banco de dados
        self.administrador_repo.deletar(administrador)
        return True
