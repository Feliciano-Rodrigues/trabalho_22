from flask import Blueprint, request, jsonify
from service.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__)
service = UsuarioService()

@usuario_bp.route('/usuarios', methods=['GET'])
def seleciona_usuarios():
    usuarios = service.listar_usuarios()
    return jsonify(usuarios)

@usuario_bp.route('/usuario/<int:id>', methods=['GET'])
def seleciona_usuario(id):
    usuario = service.buscar_usuario(id)
    if usuario:
        return jsonify(usuario)
    return jsonify({'message': 'Usuário não encontrado'}), 404

@usuario_bp.route('/usuario', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    try:
        usuario = service.criar_usuario(data)
        return jsonify(usuario), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar', 'error': str(e)}), 400

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def atualiza_usuario(id):
    data = request.get_json()
    try:
        usuario = service.atualizar_usuario(id, data)
        if usuario:
            return jsonify(usuario)
        return jsonify({'message': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar', 'error': str(e)}), 400

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def deleta_usuario(id):
    try:
        result = service.deletar_usuario(id)
        if result:
            return jsonify({'message': 'Usuário deletado'})
        return jsonify({'message': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar', 'error': str(e)}), 400
