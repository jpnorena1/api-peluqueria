# src/app.py
from flask import Flask
from controllers.clientes_controller import clientes_blueprint

app = Flask(__name__)
app.register_blueprint(clientes_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
