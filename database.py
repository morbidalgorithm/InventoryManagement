# database.py

# Biblioteca usada para conectar Python com MySQL
import mysql.connector


def connect_db():
    """
    Cria e retorna uma conexão com o banco de dados.
    Sempre que o sistema precisar acessar o banco,
    essa função será chamada.
    """

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha123",
        database="inventory"
    )

    return connection