# # entity/administrador.py
# from db import db

# class Administrador(db.Model):
#     __tablename__ = 'administradores'
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     senha = db.Column(db.String(200), nullable=False)

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "nome": self.nome,
#             "email": self.email
#         }
