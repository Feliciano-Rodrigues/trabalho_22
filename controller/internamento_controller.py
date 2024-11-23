from flask import Blueprint, request, jsonify
from service.internamento_service import InternamentoService

internamento_bp = Blueprint('internamento', __name__)
service = InternamentoService()

@internamento_bp.route('/internamentos', methods=['GET'])
def listar_internamentos():
    internamentos = service.listar_internamentos()
    return jsonify(internamentos)

@internamento_bp.route('/internamento/<int:id>', methods=['GET'])
def buscar_internamento(id):
    internamento = service.buscar_internamento(id)
    if internamento:
        return jsonify(internamento)
    return jsonify({'message': 'Internamento não encontrado'}), 404

@internamento_bp.route('/internamento', methods=['POST'])
def criar_internamento():
    data = request.get_json()
    try:
        internamento = service.criar_internamento(data)
        return jsonify(internamento), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar internamento', 'error': str(e)}), 400

@internamento_bp.route('/internamento/<int:id>', methods=['PUT'])
def atualizar_internamento(id):
    data = request.get_json()
    try:
        internamento = service.atualizar_internamento(id, data)
        if internamento:
            return jsonify(internamento)
        return jsonify({'message': 'Internamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar internamento', 'error': str(e)}), 400

@internamento_bp.route('/internamento/<int:id>', methods=['DELETE'])
def deletar_internamento(id):
    try:
        result = service.deletar_internamento(id)
        if result:
            return jsonify({'message': 'Internamento deletado'})
        return jsonify({'message': 'Internamento não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar internamento', 'error': str(e)}), 400
