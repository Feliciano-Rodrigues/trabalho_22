from db import db

class Administrador(db.Model):
    __tablename__ = 'administradores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(11), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }

    @staticmethod
    def from_dict(data):
        return Administrador(
            id=data.get('id'),
            nome=data.get('nome'),
            email=data.get('email'),
            senha=data.get('senha')
        )
