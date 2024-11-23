from db import db

class UserRepository:
    def find_by_cpf(self, cpf):
        query = "SELECT id, senha FROM usuarios WHERE cpf = %s"
        result = db.execute(query, (cpf,))
        return result.fetchone()
