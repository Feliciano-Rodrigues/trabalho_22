from db import db
class Agenda(db.Model):
    __tablename__ = 'agendas'
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinarios.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)

    veterinario = db.relationship('Veterinario', backref=db.backref('agendas', lazy=True))
    paciente = db.relationship('Paciente', backref=db.backref('agendas', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "data_hora": self.data_hora.strftime('%Y-%m-%d %H:%M:%S') if self.data_hora else None,
            "veterinario_id": self.veterinario_id,
            "paciente_id": self.paciente_id
        }

