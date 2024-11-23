import bcrypt
import jwt
import datetime
import logging

from repository.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.repository = UserRepository()
        self.secret_key = "sua_chave_secreta"
        logging.basicConfig(level=logging.DEBUG)

    def login(self, cpf, senha):
        try:
            user = self.repository.find_by_cpf(cpf)
            if not user or not bcrypt.checkpw(senha.encode('utf-8'), user['senha'].encode('utf-8')):
                raise Exception('CPF ou senha inválidos')
            
            payload = {
                'id': user['id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            return jwt.encode(payload, self.secret_key, algorithm='HS256')
        except Exception as e:
            logging.error("Erro no login: %s", str(e))
            raise
