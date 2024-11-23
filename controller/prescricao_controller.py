from flask import Blueprint, request, jsonify
from service.prescricao_service import PrescricaoService

prescricao_bp = Blueprint('prescricao', __name__)
service = PrescricaoService()

@prescricao_bp.route('/prescricoes', methods=['GET'])
def seleciona_prescricoes():
    prescricoes = service.listar_prescricoes()
    return jsonify(prescricoes)

@prescricao_bp.route('/prescricao/<int:id>', methods=['GET'])
def seleciona_prescricao(id):
    prescricao = service.buscar_prescricao(id)
    if prescricao:
        return jsonify(prescricao)
    return jsonify({'message': 'Prescrição não encontrada'}), 404

@prescricao_bp.route('/prescricao', methods=['POST'])
def criar_prescricao():
    data = request.get_json()
    try:
        prescricao = service.criar_prescricao(data)
        return jsonify(prescricao), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar prescrição', 'error': str(e)}), 400

@prescricao_bp.route('/prescricao/<int:id>', methods=['PUT'])
def atualiza_prescricao(id):
    data = request.get_json()
    try:
        prescricao = service.atualizar_prescricao(id, data)
        if prescricao:
            return jsonify(prescricao)
        return jsonify({'message': 'Prescrição não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar prescrição', 'error': str(e)}), 400

@prescricao_bp.route('/prescricao/<int:id>', methods=['DELETE'])
def deleta_prescricao(id):
    try:
        result = service.deletar_prescricao(id)
        if result:
            return jsonify({'message': 'Prescrição deletada'})
        return jsonify({'message': 'Prescrição não encontrada'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar prescrição', 'error': str(e)}), 400
