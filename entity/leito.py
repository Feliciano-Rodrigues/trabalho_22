from db import db

class Leito(db.Model):
    __tablename__ = 'leitos'
    
    id = db.Column(db.Integer, primary_key=True)
    setor = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    ocupado = db.Column(db.Boolean, default=False, nullable=False)
    id_veterinario_responsavel = db.Column(db.Integer, db.ForeignKey('veterinarios.id'))

    # Relacionamentos
    veterinario_responsavel = db.relationship('Veterinario', backref='leitos')

    def to_dict(self):
        return {
            "id": self.id,
            "setor": self.setor,
            "tipo": self.tipo,
            "ocupado": self.ocupado,
            "id_veterinario_responsavel": self.id_veterinario_responsavel
        }
