import sqlite3

connection = sqlite3.connect("clientes.db")

c = connection.cursor()

c.execute("""
    CREATE TABLE clientes(
        nome text,
        sobrenome text,
        email text,
        telefone text
          )
""")

connection.commit()
connection.close()
