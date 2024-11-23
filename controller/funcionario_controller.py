from flask import Blueprint, request, jsonify
from service.funcionario_service import FuncionarioService

funcionario_bp = Blueprint('funcionario', __name__)
service = FuncionarioService()

@funcionario_bp.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = service.listar_funcionarios()
    return jsonify(funcionarios)

@funcionario_bp.route('/funcionario/<int:id>', methods=['GET'])
def buscar_funcionario(id):
    funcionario = service.buscar_funcionario(id)
    if funcionario:
        return jsonify(funcionario)
    return jsonify({'message': 'Funcionário não encontrado'}), 404

@funcionario_bp.route('/funcionario', methods=['POST'])
def criar_funcionario():
    data = request.get_json()
    try:
        funcionario = service.criar_funcionario(data)
        return jsonify(funcionario), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar funcionário', 'error': str(e)}), 400

@funcionario_bp.route('/funcionario/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    data = request.get_json()
    try:
        funcionario = service.atualizar_funcionario(id, data)
        if funcionario:
            return jsonify(funcionario)
        return jsonify({'message': 'Funcionário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar funcionário', 'error': str(e)}), 400

@funcionario_bp.route('/funcionario/<int:id>', methods=['DELETE'])
def deletar_funcionario(id):
    try:
        result = service.deletar_funcionario(id)
        if result:
            return jsonify({'message': 'Funcionário deletado'})
        return jsonify({'message': 'Funcionário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar funcionário', 'error': str(e)}), 400

@funcionario_bp.route('/login', methods=['POST'])
def login_funcionario():
    data = request.get_json()
    try:
        funcionario = service.verificar_login(data['cpf'], data['senha'])
        if funcionario:
            token = service.gerar_token(funcionario)
            return jsonify({'token': token}), 200
        return jsonify({'message': 'Credenciais inválidas'}), 401
    except KeyError:
        return jsonify({'message': 'Campos obrigatórios ausentes: cpf, senha'}), 400
    except Exception as e:
        return jsonify({'message': 'Erro no login', 'error': str(e)}), 401

@funcionario_bp.route('/recuperar-senha', methods=['POST'])
def recuperar_senha():
    data = request.get_json()
    try:
        funcionario = service.recuperar_senha(data['cpf'], data['nova_senha'])
        if funcionario:
            return jsonify({'message': 'Senha atualizada com sucesso'}), 200
        return jsonify({'message': 'Funcionário não encontrado'}), 404
    except KeyError:
        return jsonify({'message': 'Campos obrigatórios ausentes: cpf, nova_senha'}), 400
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar senha', 'error': str(e)}), 400
