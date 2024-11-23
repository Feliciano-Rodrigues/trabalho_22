from flask import Blueprint, request, jsonify
from service.veterinario_service import VeterinarioService

veterinario_bp = Blueprint('veterinario', __name__)
service = VeterinarioService()

@veterinario_bp.route('/veterinarios', methods=['GET'])
def listar_veterinarios():
    veterinarios = service.listar_veterinarios()
    return jsonify(veterinarios)

@veterinario_bp.route('/veterinario/<int:id>', methods=['GET'])
def buscar_veterinario(id):
    veterinario = service.buscar_veterinario(id)
    if veterinario:
        return jsonify(veterinario)
    return jsonify({'message': 'Veterinário não encontrado'}), 404

@veterinario_bp.route('/veterinario', methods=['POST'])
def criar_veterinario():
    data = request.get_json()
    try:
        veterinario = service.criar_veterinario(data)
        return jsonify(veterinario), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar veterinário', 'error': str(e)}), 400

@veterinario_bp.route('/veterinario/<int:id>', methods=['PUT'])
def atualizar_veterinario(id):
    data = request.get_json()
    try:
        veterinario = service.atualizar_veterinario(id, data)
        if veterinario:
            return jsonify(veterinario)
        return jsonify({'message': 'Veterinário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar veterinário', 'error': str(e)}), 400

@veterinario_bp.route('/veterinario/<int:id>', methods=['DELETE'])
def deletar_veterinario(id):
    try:
        result = service.deletar_veterinario(id)
        if result:
            return jsonify({'message': 'Veterinário deletado'})
        return jsonify({'message': 'Veterinário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar veterinário', 'error': str(e)}), 400
