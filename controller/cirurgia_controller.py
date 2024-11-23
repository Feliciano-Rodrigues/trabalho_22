from flask import Blueprint, request, jsonify
from service.cirurgia_service import CirurgiaService

cirurgia_bp = Blueprint('cirurgia', __name__)
service = CirurgiaService()

# Criar uma cirurgia
@cirurgia_bp.route('/cirurgias', methods=['POST'])
def criar_cirurgia():
    data = request.get_json()
    try:
        cirurgia = service.criar_cirurgia(data)
        return jsonify(cirurgia), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar cirurgia', 'error': str(e)}), 400

# Listar todas as cirurgias
@cirurgia_bp.route('/cirurgias', methods=['GET'])
def listar_cirurgias():
    try:
        cirurgias = service.listar_cirurgias()
        return jsonify(cirurgias), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao listar cirurgias', 'error': str(e)}), 500

# Buscar uma cirurgia por ID
@cirurgia_bp.route('/cirurgia/<int:id>', methods=['GET'])
def buscar_cirurgia(id):
    try:
        cirurgia = service.buscar_cirurgia(id)
        if cirurgia:
            return jsonify(cirurgia), 200
        return jsonify({'message': 'Cirurgia não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao buscar cirurgia', 'error': str(e)}), 500

# Atualizar uma cirurgia
@cirurgia_bp.route('/cirurgia/<int:id>', methods=['PUT'])
def atualizar_cirurgia(id):
    data = request.get_json()
    try:
        cirurgia = service.atualizar_cirurgia(id, data)
        if cirurgia:
            return jsonify(cirurgia), 200
        return jsonify({'message': 'Cirurgia não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar cirurgia', 'error': str(e)}), 400

# Deletar uma cirurgia
@cirurgia_bp.route('/cirurgia/<int:id>', methods=['DELETE'])
def deletar_cirurgia(id):
    try:
        result = service.deletar_cirurgia(id)
        if result:
            return jsonify({'message': 'Cirurgia deletada com sucesso'}), 200
        return jsonify({'message': 'Cirurgia não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar cirurgia', 'error': str(e)}), 400
