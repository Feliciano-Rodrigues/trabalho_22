from db import db
from datetime import datetime

class Cirurgia(db.Model):
    __tablename__ = 'cirurgias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    data = db.Column(db.DateTime, nullable=False)
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinarios.id'), nullable=False)

    veterinario = db.relationship('Veterinario', backref=db.backref('cirurgias', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data": self.data.strftime('%Y-%m-%d %H:%M:%S') if self.data else None,
            "veterinario_id": self.veterinario_id
        }
