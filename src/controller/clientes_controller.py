# src/controllers/clientes_controller.py
from flask import Blueprint, jsonify, request
from models.cliente import Cliente

clientes_blueprint = Blueprint('clientes', __name__)

@clientes_blueprint.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.json
    nuevo_cliente = Cliente(data.get('nombre'), data.get('telefono'), data.get('email'))
    nuevo_cliente.guardar_en_db()
    return jsonify({'mensaje': 'Cliente agregado correctamente'}), 201
