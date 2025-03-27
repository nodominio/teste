from flask import request
import services.db_services as db_services

def cadastrar_cliente():
  try:
    dados = request.get_json()

    nome = dados.get('nome')
    idade = dados.get('idade')

    return db_services.insere_cliente_no_banco(nome, idade)

  except Exception as e:
    return {'Erro': f'Falhou: {e}'}, 500