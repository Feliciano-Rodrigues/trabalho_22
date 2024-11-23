from flask import Blueprint, request, jsonify
from service.exame_service import ExameService
from entity.exame import Exame
from datetime import datetime
from entity.consulta import Consulta

exame_bp = Blueprint('exame', __name__)
service = ExameService()

@exame_bp.route('/exames', methods=['GET'])
def listar_exames():
    exames = service.listar_exames()
    return jsonify([exame.to_dict() for exame in exames])

@exame_bp.route('/exame/<int:id>', methods=['GET'])
def buscar_exame(id):
    exame = service.buscar_exame(id)
    if exame:
        return jsonify(exame.to_dict())
    return jsonify({'message': 'Exame não encontrado'}), 404

@exame_bp.route('/exame', methods=['POST'])
def criar_exame():
    data = request.get_json()  # Recebe os dados do corpo da requisição

    # Verificação de campos obrigatórios
    if not data or 'id_consulta' not in data or 'tipo_exame' not in data or 'data_exame' not in data:
        return jsonify({'message': 'Campos obrigatórios ausentes: id_consulta, tipo_exame, data_exame'}), 400

    try:
        # Verifica se a consulta existe
        consulta = Consulta.query.get(data['id_consulta'])
        if not consulta:
            return jsonify({'message': f"Consulta com id {data['id_consulta']} não encontrada."}), 404

        # Criando o objeto Exame
        exame = Exame(
            id_consulta=data['id_consulta'],
            tipo_exame=data['tipo_exame'],
            data_exame=datetime.strptime(data['data_exame'], '%Y-%m-%dT%H:%M:%S'),
            resultado=data.get('resultado', None)
        )

        # Chama o serviço para salvar o exame
        service.criar_exame(exame)

        return jsonify(exame.to_dict()), 201  # Retorna o exame criado com status 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar exame', 'error': str(e)}), 400

@exame_bp.route('/exame/<int:id>', methods=['PUT'])
def atualizar_exame(id):
    data = request.get_json()
    try:
        exame = service.atualizar_exame(id, data)
        if exame:
            return jsonify(exame.to_dict())
        return jsonify({'message': 'Exame não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao atualizar exame', 'error': str(e)}), 400

@exame_bp.route('/exame/<int:id>', methods=['DELETE'])
def deletar_exame(id):
    try:
        result = service.deletar_exame(id)
        if result:
            return jsonify({'message': 'Exame deletado'})
        return jsonify({'message': 'Exame não encontrado'}), 404
    except Exception as e:
        return jsonify({'message': 'Erro ao deletar exame', 'error': str(e)}), 400
