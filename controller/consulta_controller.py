from flask import Blueprint, request, jsonify
from service.consulta_service import ConsultaService

consulta_bp = Blueprint('consulta', __name__)
service = ConsultaService()

@consulta_bp.route('/consultas', methods=['GET'])
def listar_consultas():
    consultas = service.listar_consultas()
    return jsonify(consultas)

@consulta_bp.route('/consulta/<int:id>', methods=['GET'])
def buscar_consulta(id):
    consulta = service.buscar_consulta(id)
    if consulta:
        return jsonify(consulta)
    return jsonify({'message': 'Consulta não encontrada'}), 404

@consulta_bp.route('/consulta', methods=['POST'])
def criar_consulta():
    data = request.get_json()
    try:
        consulta = service.criar_consulta(data)
        return jsonify(consulta), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar consulta', 'error': str(e)}), 400

@consulta_bp.route('/consulta/<int:id>', methods=['PUT'])
def atualizar_consulta(id):
    data = request.get_json()
    try:
        consulta = service.atualizar_consulta(id, data)
        if consulta:
            return jsonify(consulta)
        return jsonify({'message': 'Consulta não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar consulta', 'error': str(e)}), 400

@consulta_bp.route('/consulta/<int:id>', methods=['DELETE'])
def deletar_consulta(id):
    try:
        result = service.deletar_consulta(id)
        if result:
            return jsonify({'message': 'Consulta deletada'})
        return jsonify({'message': 'Consulta não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar consulta', 'error': str(e)}), 400
