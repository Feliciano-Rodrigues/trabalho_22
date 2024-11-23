from flask import Flask, request, jsonify
from db import init_app
from controller.usuario_controller import usuario_bp
from controller.cliente_controller import cliente_bp
from controller.consulta_controller import consulta_bp
from controller.administradores_controller import administradores_bp
from controller.agenda_controller import agenda_bp
from controller.auxiliar_veterinario_controller import auxiliar_veterinario_bp
from controller.cirurgia_controller import cirurgia_bp
from controller.estoque_controller import estoque_bp
from controller.exame_controller import exame_bp
from controller.financeiro_controller import financeiro_bp
from controller.funcionario_controller import funcionario_bp
from controller.internamento_controller import internamento_bp
from controller.medicamento_controller import medicamento_bp
from controller.paciente_controller import paciente_bp
from controller.prescricao_controller import prescricao_bp
from controller.veterinario_controller import veterinario_bp
from controller.leito_controller import leito_bp
from controller.auth_controller import auth_bp
from controller.employee_controller import employee_bp
from service.auth_service import AuthService

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/clin_44'

init_app(app)

# Registrar blueprints
app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(cliente_bp, url_prefix='/api')
app.register_blueprint(consulta_bp, url_prefix='/api')
app.register_blueprint(administradores_bp, url_prefix='/api')
app.register_blueprint(agenda_bp, url_prefix='/api')
app.register_blueprint(auxiliar_veterinario_bp, url_prefix='/api')
app.register_blueprint(cirurgia_bp, url_prefix='/api')
app.register_blueprint(estoque_bp, url_prefix='/api')
app.register_blueprint(exame_bp, url_prefix='/api')
app.register_blueprint(financeiro_bp, url_prefix='/api')
app.register_blueprint(funcionario_bp, url_prefix='/api')
app.register_blueprint(internamento_bp, url_prefix='/api')
app.register_blueprint(medicamento_bp, url_prefix='/api')
app.register_blueprint(paciente_bp, url_prefix='/api')
app.register_blueprint(prescricao_bp, url_prefix='/api')
app.register_blueprint(veterinario_bp, url_prefix='/api')
app.register_blueprint(leito_bp, url_prefix='/api')
app.register_blueprint(employee_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

# Rota de login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'cpf' not in data or 'senha' not in data:
        return jsonify({'message': 'Campos obrigatórios ausentes: cpf, senha'}), 400

    cpf = data['cpf']
    senha = data['senha']

    auth_service = AuthService()  # Chama o serviço de autenticação
    token = auth_service.login(cpf, senha)  # Tenta autenticar e gerar o token

    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'CPF ou senha inválidos'}), 401

if __name__ == "__main__":
    app.run(debug=True)
