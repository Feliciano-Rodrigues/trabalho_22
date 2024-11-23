from db import db

class Consulta(db.Model):
    __tablename__ = 'consultas'
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    id_veterinario = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    data_consulta = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    # Relacionamento com a tabela Prescricao
    prescricoes = db.relationship('Prescricao', backref='consulta', lazy=True)
    paciente = db.relationship('Paciente', backref='consultas')
    veterinario = db.relationship('Funcionario', backref='consultas')

    def to_dict(self):
        return {
            "id": self.id,
            "id_paciente": self.id_paciente,
            "id_veterinario": self.id_veterinario,
            "data_consulta": self.data_consulta.isoformat(),
            "descricao": self.descricao,
        }
