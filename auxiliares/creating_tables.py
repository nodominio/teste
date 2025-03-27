import sqlite3

conexao = sqlite3.connect('client.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(256), idade VARCHAR(3));''')

conexao.commit()