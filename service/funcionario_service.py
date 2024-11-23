import bcrypt
import jwt
import datetime

from repository.funcionario_repository import FuncionarioRepository
from entity.funcionario import Funcionario

class FuncionarioService:
    def __init__(self):
        self.repository = FuncionarioRepository()
        self.secret_key = "sua_chave_secreta"

    def criar_funcionario(self, data):
        hashed_senha = bcrypt.hashpw(data['senha'].encode('utf-8'), bcrypt.gensalt())
        funcionario = Funcionario(
            nome=data['nome'],
            cpf=data['cpf'],
            senha=hashed_senha.decode('utf-8')
        )
        return self.repository.salvar(funcionario)

    def listar_funcionarios(self):
        return self.repository.listar_todos()

    def buscar_funcionario(self, id):
        return self.repository.buscar_por_id(id)

    def atualizar_funcionario(self, id, data):
        funcionario = self.repository.buscar_por_id(id)
        if not funcionario:
            return None
        if 'nome' in data:
            funcionario.nome = data['nome']
        if 'cpf' in data:
            funcionario.cpf = data['cpf']
        if 'senha' in data:
            funcionario.senha = bcrypt.hashpw(data['senha'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.repository.atualizar(funcionario)

    def deletar_funcionario(self, id):
        funcionario = self.repository.buscar_por_id(id)
        if funcionario:
            self.repository.deletar(funcionario)
            return True
        return False

    def verificar_login(self, cpf, senha):
        funcionario = self.repository.buscar_por_cpf(cpf)
        if funcionario and bcrypt.checkpw(senha.encode('utf-8'), funcionario['senha'].encode('utf-8')):
            return funcionario
        return None

    def gerar_token(self, funcionario):
        payload = {
            'id': funcionario['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def recuperar_senha(self, cpf, nova_senha):
        funcionario = self.repository.buscar_por_cpf(cpf)
        if funcionario:
            hashed_senha = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            funcionario.senha = hashed_senha
            self.repository.atualizar(funcionario)
            return funcionario
        return None
