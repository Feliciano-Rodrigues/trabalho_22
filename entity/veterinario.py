from db import db

class Veterinario(db.Model):
    __tablename__ = 'veterinarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    crmv = db.Column(db.String(50), unique=True, nullable=False)  # Registro profissional do veterinário
    telefone = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "crmv": self.crmv,
            "telefone": self.telefone,
            "email": self.email,
            "endereco": self.endereco
        }
