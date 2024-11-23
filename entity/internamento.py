from db import db

class Internamento(db.Model):
    __tablename__ = 'internamentos'
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    id_leito = db.Column(db.Integer, db.ForeignKey('leitos.id'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    motivo = db.Column(db.Text, nullable=False)

    paciente = db.relationship('Paciente', backref='internamentos')
    leito = db.relationship('Leito', backref='internamentos')

    def to_dict(self):
        return {
            "id": self.id,
            "id_paciente": self.id_paciente,
            "id_leito": self.id_leito,
            "data_inicio": str(self.data_inicio),
            "data_fim": str(self.data_fim) if self.data_fim else None,
            "motivo": self.motivo,
        }
