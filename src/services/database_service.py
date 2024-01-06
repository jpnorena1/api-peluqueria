# src/services/database_service.py
from models.database import Database

class DatabaseService:
    def __enter__(self):
        return Database()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
