from datetime import datetime
from repository.agenda_repository import AgendaRepository
from entity.agenda import Agenda

class AgendaService:
    def __init__(self):
        self.agenda_repo = AgendaRepository()

    def listar_agendas(self):
        # Convertendo cada objeto Agenda para dicionário
        agendas = self.agenda_repo.listar_agendas()
        return [agenda.to_dict() for agenda in agendas]

    def buscar_agenda(self, id):
        agenda = self.agenda_repo.buscar_agenda(id)
        return agenda.to_dict() if agenda else None

    def criar_agenda(self, data):
        try:
            agenda = Agenda(
                data_hora=datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S'),
                veterinario_id=data['veterinario_id'],
                paciente_id=data['paciente_id']
            )
            agenda = self.agenda_repo.criar_agenda(agenda)
            return agenda.to_dict()  # Convertendo para dicionário
        except Exception as e:
            raise ValueError(f"Erro ao criar agenda: {str(e)}")

    def atualizar_agenda(self, id, data):
        agenda = self.agenda_repo.buscar_agenda(id)
        if not agenda:
            return None

        # Atualizando os campos da agenda
        agenda.data_hora = datetime.strptime(data.get('data_hora', agenda.data_hora.strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')
        agenda.veterinario_id = data.get('veterinario_id', agenda.veterinario_id)
        agenda.paciente_id = data.get('paciente_id', agenda.paciente_id)

        agenda = self.agenda_repo.atualizar_agenda(agenda)
        return agenda.to_dict()  # Convertendo para dicionário

    def deletar_agenda(self, id):
        agenda = self.agenda_repo.buscar_agenda(id)
        if not agenda:
            return False
        self.agenda_repo.deletar_agenda(agenda)
        return True
