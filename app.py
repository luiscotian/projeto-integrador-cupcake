from flask import Flask, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder='templates', static_folder='static')

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='loja_cupcakes',
            user='root',
            password='Valentim20!' # <--- MUDE PARA A SUA SENHA DO MYSQL
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(produtos)
    return jsonify({'erro': 'Falha na conexão com o banco de dados'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)