from db import db

class EmployeeRepository:
    def insert(self, data):
        query = "INSERT INTO funcionarios (nome, cpf, cargo) VALUES (%s, %s, %s)"
        db.execute(query, (data['nome'], data['cpf'], data['cargo']))
