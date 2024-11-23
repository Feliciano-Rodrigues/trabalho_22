from db import db
from entity.exame import Exame
from datetime import datetime

class ExameService:
    def listar_exames(self):
        # Retorna todos os exames
        return Exame.query.all()

    def buscar_exame(self, id):
        # Busca um exame pelo ID
        return Exame.query.get(id)

    def criar_exame(self, exame):
        try:
            db.session.add(exame)  # Adiciona o exame à sessão do banco de dados
            db.session.commit()     # Faz o commit para persistir os dados
        except Exception as e:
            db.session.rollback()   # Em caso de erro, faz o rollback
            raise ValueError(f"Erro ao criar exame: {str(e)}")

    def atualizar_exame(self, id, data):
        exame = Exame.query.get(id)
        if not exame:
            return None

        exame.tipo_exame = data.get('tipo_exame', exame.tipo_exame)
        exame.data_exame = datetime.strptime(data.get('data_exame', exame.data_exame.isoformat()), '%Y-%m-%dT%H:%M:%S')
        exame.resultado = data.get('resultado', exame.resultado)

        try:
            db.session.commit()
            return exame
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao atualizar exame: {str(e)}")

    def deletar_exame(self, id):
        exame = Exame.query.get(id)
        if exame:
            try:
                db.session.delete(exame)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Erro ao deletar exame: {str(e)}")
        return False
