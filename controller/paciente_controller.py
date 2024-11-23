from flask import Blueprint, request, jsonify
from service.paciente_service import PacienteService

paciente_bp = Blueprint('paciente', __name__)
service = PacienteService()

@paciente_bp.route('/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = service.listar_pacientes()
    return jsonify(pacientes)

@paciente_bp.route('/paciente/<int:id>', methods=['GET'])
def buscar_paciente(id):
    paciente = service.buscar_paciente(id)
    if paciente:
        return jsonify(paciente)
    return jsonify({'message': 'Paciente não encontrado'}), 404

@paciente_bp.route('/paciente', methods=['POST'])
def criar_paciente():
    data = request.get_json()
    try:
        paciente = service.criar_paciente(data)
        return jsonify(paciente), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar paciente', 'error': str(e)}), 400

@paciente_bp.route('/paciente/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    data = request.get_json()
    try:
        paciente = service.atualizar_paciente(id, data)
        if paciente:
            return jsonify(paciente)
        return jsonify({'message': 'Paciente não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar paciente', 'error': str(e)}), 400

@paciente_bp.route('/paciente/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    try:
        result = service.deletar_paciente(id)
        if result:
            return jsonify({'message': 'Paciente deletado'})
        return jsonify({'message': 'Paciente não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar paciente', 'error': str(e)}), 400
