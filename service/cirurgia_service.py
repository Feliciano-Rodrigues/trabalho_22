from datetime import datetime
from repository.cirurgia_repository import CirurgiaRepository
from entity.cirurgia import Cirurgia

class CirurgiaService:
    def __init__(self):
        self.cirurgia_repo = CirurgiaRepository()

    def listar_cirurgias(self):
        cirurgias = self.cirurgia_repo.listar_cirurgias()
        return [cirurgia.to_dict() for cirurgia in cirurgias]

    def buscar_cirurgia(self, id):
        cirurgia = self.cirurgia_repo.buscar_cirurgia(id)
        return cirurgia.to_dict() if cirurgia else None

    def criar_cirurgia(self, data):
        try:
            data_hora = data['data'].replace("T", " ")  # Ajustando para ISO 8601
            cirurgia = Cirurgia(
                nome=data['nome'],
                descricao=data.get('descricao'),
                data=datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S'),
                veterinario_id=data['veterinario_id']
            )
            cirurgia_criada = self.cirurgia_repo.criar_cirurgia(cirurgia)
            return cirurgia_criada.to_dict()  # Transformando em dicionário antes de retornar
        except Exception as e:
            raise ValueError(f"Erro ao criar cirurgia: {str(e)}")

    def atualizar_cirurgia(self, id, data):
        cirurgia = self.cirurgia_repo.buscar_cirurgia(id)
        if not cirurgia:
            return None

        # Atualizando os campos da cirurgia
        cirurgia.nome = data.get('nome', cirurgia.nome)
        cirurgia.descricao = data.get('descricao', cirurgia.descricao)
        cirurgia.data = datetime.strptime(data.get('data', cirurgia.data.strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')
        cirurgia.veterinario_id = data.get('veterinario_id', cirurgia.veterinario_id)

        cirurgia = self.cirurgia_repo.atualizar_cirurgia(cirurgia)
        return cirurgia.to_dict()  # Retorna como dicionário

    def deletar_cirurgia(self, id):
        cirurgia = self.cirurgia_repo.buscar_cirurgia(id)
        if not cirurgia:
            return False
        self.cirurgia_repo.deletar_cirurgia(cirurgia)
        return True
