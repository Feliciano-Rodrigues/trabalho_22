from flask import Blueprint, request, jsonify
from service.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    cpf = data.get('cpf')
    senha = data.get('senha')

    if not cpf or not senha:
        return jsonify({'message': 'CPF e senha são obrigatórios'}), 400

    try:
        token = auth_service.login(cpf, senha)
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'message': 'Erro no login', 'error': str(e)}), 401
