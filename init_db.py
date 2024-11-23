from app import app
from db import db, init_app

def initialize_database():
    init_app(app)
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    initialize_database()

    
