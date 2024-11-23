from flask import Blueprint, request, jsonify
from service.medicamento_service import MedicamentoService

medicamento_bp = Blueprint('medicamento', __name__)
service = MedicamentoService()

@medicamento_bp.route('/medicamentos', methods=['GET'])
def listar_medicamentos():
    medicamentos = service.listar_medicamentos()
    return jsonify(medicamentos)

@medicamento_bp.route('/medicamento/<int:id>', methods=['GET'])
def buscar_medicamento(id):
    medicamento = service.buscar_medicamento(id)
    if medicamento:
        return jsonify(medicamento)
    return jsonify({'message': 'Medicamento não encontrado'}), 404

@medicamento_bp.route('/medicamento', methods=['POST'])
def criar_medicamento():
    data = request.get_json()
    try:
        medicamento = service.criar_medicamento(data)
        return jsonify(medicamento), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar medicamento', 'error': str(e)}), 400

@medicamento_bp.route('/medicamento/<int:id>', methods=['PUT'])
def atualizar_medicamento(id):
    data = request.get_json()
    try:
        medicamento = service.atualizar_medicamento(id, data)
        if medicamento:
            return jsonify(medicamento)
        return jsonify({'message': 'Medicamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar medicamento', 'error': str(e)}), 400

@medicamento_bp.route('/medicamento/<int:id>', methods=['DELETE'])
def deletar_medicamento(id):
    try:
        result = service.deletar_medicamento(id)
        if result:
            return jsonify({'message': 'Medicamento deletado'})
        return jsonify({'message': 'Medicamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar medicamento', 'error': str(e)}), 400
