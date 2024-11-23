# controller/financeiro_controller.py
from flask import Blueprint, request, jsonify
from service.financeiro_service import FinanceiroService

financeiro_bp = Blueprint('financeiro', __name__)
service = FinanceiroService()

@financeiro_bp.route('/financeiros', methods=['GET'])
def listar_financeiros():
    financeiros = service.listar_financeiros()
    return jsonify([financeiro.to_dict() for financeiro in financeiros])

@financeiro_bp.route('/financeiro/<int:id>', methods=['GET'])
def buscar_financeiro(id):
    financeiro = service.buscar_financeiro(id)
    if financeiro:
        return jsonify(financeiro.to_dict())
    return jsonify({'message': 'Financeiro não encontrado'}), 404

@financeiro_bp.route('/financeiro', methods=['POST'])
def criar_financeiro():
    data = request.get_json()  # Recebe os dados do corpo da requisição

    # Verificação de campos obrigatórios
    if not data or 'tipo' not in data or 'valor' not in data or 'data' not in data:
        return jsonify({'message': 'Campos obrigatórios ausentes: tipo, valor, data'}), 400

    try:
        financeiro = service.criar_financeiro(data)
        return jsonify(financeiro.to_dict()), 201  # Retorna o financeiro criado com status 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar financeiro', 'error': str(e)}), 400

@financeiro_bp.route('/financeiro/<int:id>', methods=['PUT'])
def atualizar_financeiro(id):
    data = request.get_json()
    try:
        financeiro = service.atualizar_financeiro(id, data)
        if financeiro:
            return jsonify(financeiro.to_dict())
        return jsonify({'message': 'Financeiro não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar financeiro', 'error': str(e)}), 400

@financeiro_bp.route('/financeiro/<int:id>', methods=['DELETE'])
def deletar_financeiro(id):
    try:
        result = service.deletar_financeiro(id)
        if result:
            return jsonify({'message': 'Financeiro deletado'})
        return jsonify({'message': 'Financeiro não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar financeiro', 'error': str(e)}), 400
