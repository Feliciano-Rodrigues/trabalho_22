from repository.paciente_repository import PacienteRepository
from entity.paciente import Paciente

class PacienteService:
    def __init__(self):
        self.repository = PacienteRepository()

    def criar_paciente(self, data):
        """
        Cria um novo paciente com base nos dados fornecidos.
        """
        try:
            paciente = Paciente(
                nome=data['nome'],
                especie=data['especie'],
                raca=data['raca'],
                idade=data['idade'],
                peso=data['peso'],
                historico_medico=data['historico_medico'] if 'historico_medico' in data else ""
            )
            self.repository.salvar(paciente)
            return {"mensagem": "Paciente criado com sucesso!", "paciente": paciente.to_dict()}
        except Exception as e:
            print(f"Erro ao criar paciente: {e}")
            return {"mensagem": "Erro ao criar paciente", "erro": str(e)}

    def listar_pacientes(self):
        """
        Retorna uma lista de todos os pacientes cadastrados.
        """
        try:
            pacientes = self.repository.buscar_todos()
            return [paciente.to_dict() for paciente in pacientes]
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
            return {"mensagem": "Erro ao listar pacientes", "erro": str(e)}

    def buscar_paciente_por_id(self, paciente_id):
        """
        Retorna os dados de um paciente específico pelo ID.
        """
        try:
            paciente = self.repository.buscar_por_id(paciente_id)
            if paciente:
                return paciente.to_dict()
            return {"mensagem": "Paciente não encontrado"}
        except Exception as e:
            print(f"Erro ao buscar paciente: {e}")
            return {"mensagem": "Erro ao buscar paciente", "erro": str(e)}

    def atualizar_paciente(self, paciente_id, data):
        """
        Atualiza as informações de um paciente específico.
        """
        try:
            paciente = self.repository.buscar_por_id(paciente_id)
            if not paciente:
                return {"mensagem": "Paciente não encontrado"}

            # Atualiza os campos permitidos
            if 'nome' in data:
                paciente.nome = data['nome']
            if 'especie' in data:
                paciente.especie = data['especie']
            if 'raca' in data:
                paciente.raca = data['raca']
            if 'idade' in data:
                paciente.idade = data['idade']
            if 'peso' in data:
                paciente.peso = data['peso']
            if 'historico_medico' in data:
                paciente.historico_medico = data['historico_medico']

            self.repository.salvar(paciente)
            return {"mensagem": "Paciente atualizado com sucesso!", "paciente": paciente.to_dict()}
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")
            return {"mensagem": "Erro ao atualizar paciente", "erro": str(e)}

    def deletar_paciente(self, paciente_id):
        """
        Remove um paciente do sistema pelo ID.
        """
        try:
            paciente = self.repository.buscar_por_id(paciente_id)
            if not paciente:
                return {"mensagem": "Paciente não encontrado"}

            self.repository.deletar(paciente_id)
            return {"mensagem": "Paciente deletado com sucesso!"}
        except Exception as e:
            print(f"Erro ao deletar paciente: {e}")
            return {"mensagem": "Erro ao deletar paciente", "erro": str(e)}
