# product_service.py

# Importa função de conexão
from database import connect_db


def add_product(name, quantity, price):
    """
    Insere um produto no banco de dados.
    """

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO products (name, quantity, price)
    VALUES (%s,%s,%s)
    """

    cursor.execute(query, (name, quantity, price))

    conn.commit()
    conn.close()


def get_products():
    """
    Retorna todos os produtos cadastrados.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return products


def update_product(product_id, name, quantity, price):
    """
    Atualiza um produto existente.
    """

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    UPDATE products
    SET name=%s, quantity=%s, price=%s
    WHERE id=%s
    """

    cursor.execute(query, (name, quantity, price, product_id))

    conn.commit()
    conn.close()


def delete_product(product_id):
    """
    Remove um produto do banco de dados.
    """

    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM products WHERE id=%s"

    cursor.execute(query, (product_id,))

    conn.commit()
    conn.close()


def search_products(term):
    """
    Procura produtos pelo nome.
    """

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE name LIKE %s"

    cursor.execute(query, (f"%{term}%",))

    results = cursor.fetchall()

    conn.close()

    return results