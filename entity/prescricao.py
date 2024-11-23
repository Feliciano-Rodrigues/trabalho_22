from db import db

class Prescricao(db.Model):
    __tablename__ = 'prescricoes'
    id = db.Column(db.Integer, primary_key=True)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=False)
    medicamento = db.Column(db.String(100), nullable=False)
    dosagem = db.Column(db.String(50), nullable=False)
    frequencia = db.Column(db.String(50), nullable=False)
    duracao = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.String(200), nullable=True)
    # consulta = db.relationship("Consulta", back_populates="prescricoes")

    def to_dict(self):
        return {
            "id": self.id,
            "id_consulta": self.id_consulta,
            "medicamento": self.medicamento,
            "dosagem": self.dosagem,
            "frequencia": self.frequencia,
            "duracao": self.duracao,
            "observacoes": self.observacoes,
        }
    
