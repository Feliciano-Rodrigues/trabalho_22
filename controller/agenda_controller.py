from flask import Blueprint, request, jsonify
from service.agenda_service import AgendaService

agenda_bp = Blueprint('agenda', __name__)
service = AgendaService()

@agenda_bp.route('/agendas', methods=['GET'])
def listar_agendas():
    try:
        agendas = service.listar_agendas()
        return jsonify(agendas), 200  # Código de status 200 para sucesso
    except Exception as e:
        return jsonify({'message': 'Erro ao listar agendas', 'error': str(e)}), 500

@agenda_bp.route('/agenda/<int:id>', methods=['GET'])
def buscar_agenda(id):
    try:
        agenda = service.buscar_agenda(id)
        if agenda:
            return jsonify(agenda), 200
        return jsonify({'message': 'Agenda não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao buscar agenda', 'error': str(e)}), 500

@agenda_bp.route('/agenda', methods=['POST'])
def criar_agenda():
    data = request.get_json()
    try:
        agenda = service.criar_agenda(data)
        return jsonify(agenda), 201  # Código de status 201 para recurso criado
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar agenda', 'error': str(e)}), 400

@agenda_bp.route('/agenda/<int:id>', methods=['PUT'])
def atualizar_agenda(id):
    data = request.get_json()
    try:
        agenda = service.atualizar_agenda(id, data)
        if agenda:
            return jsonify(agenda), 200
        return jsonify({'message': 'Agenda não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar agenda', 'error': str(e)}), 400

@agenda_bp.route('/agenda/<int:id>', methods=['DELETE'])
def deletar_agenda(id):
    try:
        result = service.deletar_agenda(id)
        if result:
            return jsonify({'message': 'Agenda deletada'}), 200
        return jsonify({'message': 'Agenda não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar agenda', 'error': str(e)}), 400
