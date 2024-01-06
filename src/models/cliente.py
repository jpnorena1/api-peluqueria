# src/models/cliente.py
from models.database import Database

class Cliente:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def guardar_en_db(self):
        with Database() as db:
            db.cursor.execute('INSERT INTO clientes (nombre, telefono, email) VALUES (%s, %s, %s)',
                              (self.nombre, self.telefono, self.email))
            db.conn.commit()
