# entity/financeiro.py
from db import db

class Financeiro(db.Model):
    __tablename__ = 'financeiros'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # Exemplo: 'Receita', 'Despesa'
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "valor": self.valor,
            "data": self.data,
            "descricao": self.descricao
        }
