from db import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(15))
    contato_emergencial = db.Column(db.String(15))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "contato_emergencial": self.contato_emergencial
        }
