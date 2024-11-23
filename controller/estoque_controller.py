from flask import Blueprint, request, jsonify
from service.estoque_service import EstoqueService

estoque_bp = Blueprint('estoque', __name__)
service = EstoqueService()

@estoque_bp.route('/estoques', methods=['GET'])
def listar_estoques():
    estoques = service.listar_estoques()
    return jsonify(estoques)

@estoque_bp.route('/estoque/<int:id>', methods=['GET'])
def buscar_estoque(id):
    estoque = service.buscar_estoque(id)
    if estoque:
        return jsonify(estoque)
    return jsonify({'message': 'Estoque não encontrado'}), 404

@estoque_bp.route('/estoque', methods=['POST'])
def criar_estoque():
    data = request.get_json()
    try:
        estoque = service.criar_estoque(data)
        return jsonify(estoque), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar estoque', 'error': str(e)}), 400

@estoque_bp.route('/estoque/<int:id>', methods=['PUT'])
def atualizar_estoque(id):
    data = request.get_json()
    try:
        estoque = service.atualizar_estoque(id, data)
        if estoque:
            return jsonify(estoque)
        return jsonify({'message': 'Estoque não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar estoque', 'error': str(e)}), 400

@estoque_bp.route('/estoque/<int:id>', methods=['DELETE'])
def deletar_estoque(id):
    try:
        result = service.deletar_estoque(id)
        if result:
            return jsonify({'message': 'Estoque deletado'})
        return jsonify({'message': 'Estoque não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar estoque', 'error': str(e)}), 400
