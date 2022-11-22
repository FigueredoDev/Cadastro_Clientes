import sqlite3
import tkinter as tk

import pandas as pd


# Inserindo os dados dentro do banco
def register_client():
    connection = sqlite3.connect("clientes.db")
    c = connection.cursor()

    c.execute(
        " INSERT INTO clientes VALUES (:nome, :sobrenome,:email,:telefone)",
        {
            "nome": entry_name.get(),
            "sobrenome": entry_lastname.get(),
            "email": entry_email.get(),
            "telefone": entry_phone_number.get(),
        }
    )

    connection.commit()
    connection.close()

    entry_name.delete(0, "end")
    entry_lastname.delete(0, "end")
    entry_email.delete(0, "end")
    entry_phone_number.delete(0, "end")


# Exportando clientes para planilha
def export_clients():
    connection = sqlite3.connect("clientes.db")
    c = connection.cursor()

    c.execute("SELECT *, oid FROM clientes")
    registered_costumers = c.fetchall()
    registered_costumers = pd.DataFrame(
        registered_costumers,
        columns=["nome", "sobrenome", "email", "telefone", "ID_BANCO"]
    )

    registered_costumers.to_excel("banco_clientes.xlsx", index=False)

    connection.commit()
    connection.close()


window = tk.Tk()

window.title("Cadastro de clientes")

# labels

label_nome = tk.Label(window, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(window, text="Sobrenome")
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(window, text="Email")
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(window, text="Telefone")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# entry's

entry_name = tk.Entry(window, text="Nome", width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

entry_lastname = tk.Entry(window, text="Sobrenome", width=30)
entry_lastname.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(window, text="Email", width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_phone_number = tk.Entry(window, text="Telefone", width=30)
entry_phone_number.grid(row=3, column=1, padx=10, pady=10)

# buttons

button_register = tk.Button(
    window, text="Cadastrar Cliente", command=register_client)
button_register.grid(row=4, column=0, padx=10,
                     pady=10, ipadx=105, columnspan=2)

button_export = tk.Button(
    window, text="Exportar base de clientes", command=export_clients)
button_export.grid(row=5, column=0, padx=10, pady=10, ipadx=80, columnspan=2)

window.mainloop()
