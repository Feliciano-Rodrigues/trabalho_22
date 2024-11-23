from flask import Blueprint, request, jsonify
from service.leito_service import LeitoService

leito_bp = Blueprint('leito', __name__)
service = LeitoService()

@leito_bp.route('/leitos', methods=['GET'])
def listar_leitos():
    leitos = service.listar_leitos()
    return jsonify(leitos)

@leito_bp.route('/leito/<int:id>', methods=['GET'])
def buscar_leito(id):
    leito = service.buscar_leito(id)
    if leito:
        return jsonify(leito)
    return jsonify({'message': 'Leito não encontrado'}), 404

@leito_bp.route('/leito', methods=['POST'])
def criar_leito():
    data = request.get_json()
    try:
        leito = service.criar_leito(data)
        return jsonify(leito), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao criar leito', 'error': str(e)}), 400

@leito_bp.route('/leito/<int:id>', methods=['PUT'])
def atualizar_leito(id):
    data = request.get_json()
    try:
        leito = service.atualizar_leito(id, data)
        if leito:
            return jsonify(leito)
        return jsonify({'message': 'Leito não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar leito', 'error': str(e)}), 400

@leito_bp.route('/leito/<int:id>', methods=['DELETE'])
def deletar_leito(id):
    try:
        result = service.deletar_leito(id)
        if result:
            return jsonify({'message': 'Leito deletado'})
        return jsonify({'message': 'Leito não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar leito', 'error': str(e)}), 400
