from db import db


class Estoque(db.Model):
    __tablename__ = 'estoques'
    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False) # formato de data errado
    data_validade = db.Column(db.Date, nullable=True) # formato de data errada
    

    def to_dict(self):
        return {
            "id": self.id,
            "nome_produto": self.nome_produto,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "data_entrada": self.data_entrada,
            "data_validade": self.data_validade
        }
