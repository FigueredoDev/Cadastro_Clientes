import sqlite3

conexao = sqlite3.connect("clientes.db")

c = conexao.cursor()

c.execute("""
    CREATE TABLE clientes(
        nome text,
        sobrenome text,
        email text, 
        telefone text
          )        
""")

conexao.commit()
conexao.close()
