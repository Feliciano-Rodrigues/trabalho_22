from flask import Blueprint, request, jsonify
from service.administradores_service import AdministradoresService

administradores_bp = Blueprint('administradores', __name__)
service = AdministradoresService()

@administradores_bp.route('/administradores', methods=['GET'])
def listar_administradores():
    administradores = service.listar_administradores()
    return jsonify(administradores)

@administradores_bp.route('/administrador/<int:id>', methods=['GET'])
def buscar_administrador(id):
    administrador = service.buscar_administrador(id)
    if administrador:
        return jsonify(administrador)
    return jsonify({'message': 'Administrador não encontrado'}), 404

@administradores_bp.route('/administrador', methods=['POST'])
def criar_administrador():
    data = request.get_json()
    try:
        administrador = service.criar_administrador(data)
        return jsonify(administrador), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar administrador', 'error': str(e)}), 400

@administradores_bp.route('/administrador/<int:id>', methods=['PUT'])
def atualizar_administrador(id):
    data = request.get_json()
    try:
        administrador = service.atualizar_administrador(id, data)
        if administrador:
            return jsonify(administrador)
        return jsonify({'message': 'Administrador não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar administrador', 'error': str(e)}), 400

@administradores_bp.route('/administrador/<int:id>', methods=['DELETE'])
def deletar_administrador(id):
    try:
        result = service.deletar_administrador(id)
        if result:
            return jsonify({'message': 'Administrador deletado'})
        return jsonify({'message': 'Administrador não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar administrador', 'error': str(e)}), 400
