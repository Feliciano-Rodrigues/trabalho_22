from flask import Blueprint, request, jsonify
from service.auxiliar_veterinario_service import AuxiliarVeterinarioService

auxiliar_veterinario_bp = Blueprint('auxiliar_veterinario', __name__)
service = AuxiliarVeterinarioService()

@auxiliar_veterinario_bp.route('/auxiliares_veterinarios', methods=['GET'])
def listar_auxiliares():
    try:
        auxiliares = service.listar_auxiliares()
        return jsonify(auxiliares), 200  # Adicionado o código de status 200
    except Exception as e:
        return jsonify({'message': 'Erro ao listar auxiliares veterinários', 'error': str(e)}), 500

@auxiliar_veterinario_bp.route('/auxiliar_veterinario/<int:id>', methods=['GET'])
def buscar_auxiliar(id):
    try:
        auxiliar = service.buscar_auxiliar(id)
        if auxiliar:
            return jsonify(auxiliar), 200
        return jsonify({'message': 'Auxiliar Veterinário não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao buscar auxiliar veterinário', 'error': str(e)}), 500
