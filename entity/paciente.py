from db import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    especie = db.Column(db.String(50))
    raca = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    peso = db.Column(db.Float)
    historico_medico = db.Column(db.Text)
    alergias = db.Column(db.Text)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

    cliente = db.relationship('Cliente', backref='pacientes')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "raca": self.raca,
            "idade": self.idade,
            "peso": self.peso,
            "historico_medico": self.historico_medico,
            "alergias": self.alergias,
            "cliente_id": self.cliente_id
        }
