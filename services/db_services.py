import sqlite3

connect = sqlite3.connect('client.db')
cursor = connect.cursor()

def insere_cliente_no_banco(nome:str, idade:str):
  try:
    comando_insert = '''INSERT INTO cliente (nome, idade) VALUES (?, ?)'''
    cursor.execute(comando_insert, (nome, idade))
    connect.commit()
    connect.close()
    return {'mensagem': 'Deu certo'}, 200
  except Exception as e:
    return {'Erro': f'Falhou: {e}'}, 500



def exibir_clientes_do_banco():
  clientes = []
  try:
    comando_select = '''SELECT * FROM cliente'''
    cursor.execute(comando_select)
    colunas = cursor.fetchall()
    for coluna in colunas:
      cliente = {'id': coluna[0], 'nome': coluna[1], 'idade': coluna[2]}
      clientes.append(cliente)
    return clientes
  except Exception as e:
    return {'Erro': f'Falhou: {e}'}, 500