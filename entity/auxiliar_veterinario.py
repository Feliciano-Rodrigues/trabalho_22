# entity/auxiliar_veterinario.py
from db import db

class AuxiliarVeterinario(db.Model):
    __tablename__ = 'auxiliares_veterinarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=True)
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinarios.id'), nullable=False)

    veterinario = db.relationship('Veterinario', backref=db.backref('auxiliares', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "veterinario_id": self.veterinario_id
        }
