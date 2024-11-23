from flask import Blueprint, request, jsonify
from service.employee_service import EmployeeService

employee_bp = Blueprint('employee', __name__)
employee_service = EmployeeService()

@employee_bp.route('/create', methods=['POST'])
def create_employee():
    data = request.get_json()

    try:
        employee_service.create_employee(data)
        return jsonify({'message': 'Funcionário cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao cadastrar funcionário', 'error': str(e)}), 400
