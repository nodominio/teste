from flask import Flask, jsonify
import services.db_services as db_services
import services.client_services as client_services

app = Flask(__name__)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
  return client_services.cadastrar_cliente()

@app.route('/exibir_clientes', methods=['GET'])
def exibir_clientes():
  clientes = db_services.exibir_clientes_do_banco()
  return jsonify(clientes)

@app.route('/atualizar_cliente', methods=['PUT'])
def atualizar_cliente():
  return db_services.atualizar_cliente()

@app.route('/deletar_cliente', methods=['DELETE'])
def deletar_cliente():
  return db_services.deletar_cliente()

if __name__ == '__main__':
  app.run(debug=True)