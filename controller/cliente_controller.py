from flask import Blueprint, request, jsonify
from service.cliente_service import ClienteService

cliente_bp = Blueprint('cliente', __name__)
service = ClienteService()

@cliente_bp.route('/clientes', methods=['GET'])
def seleciona_clientes():
    clientes = service.listar_clientes()
    return jsonify(clientes)

@cliente_bp.route('/cliente/<int:id>', methods=['GET'])
def seleciona_cliente(id):
    cliente = service.buscar_cliente(id)
    if cliente:
        return jsonify(cliente)
    return jsonify({'message': 'Cliente não encontrado'}), 404

@cliente_bp.route('/cliente', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    try:
        cliente = service.criar_cliente(data)
        return jsonify(cliente), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar', 'error': str(e)}), 400

@cliente_bp.route('/cliente/<int:id>', methods=['PUT'])
def atualiza_cliente(id):
    data = request.get_json()
    try:
        cliente = service.atualizar_cliente(id, data)
        if cliente:
            return jsonify(cliente)
        return jsonify({'message': 'Cliente não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar', 'error': str(e)}), 400

@cliente_bp.route('/cliente/<int:id>', methods=['DELETE'])
def deleta_cliente(id):
    try:
        result = service.deletar_cliente(id)
        if result:
            return jsonify({'message': 'Cliente deletado'})
        return jsonify({'message': 'Cliente não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar', 'error': str(e)}), 400
