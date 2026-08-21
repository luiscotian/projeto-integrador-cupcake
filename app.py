import sqlite3
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates')

def conectar_bd():
    conn = sqlite3.connect('loja_cupcakes.db')
    conn.row_factory = sqlite3.Row  # Retorna resultados como dicionários
    return conn

def inicializar_bd():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            imagem_url TEXT
        )
    ''')
    
    # Verifica se a tabela está vazia para popular com os novos sabores saudáveis
    cursor.execute("SELECT COUNT(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        produtos_iniciais = [
            ('Cupcake de Maçã com Canela', 'Massa fofinha adoçada 100% com purê de maçã natural e um toque de canela.', 13.50, 'maca.jpg'),
            ('Cupcake de Banana com Aveia', 'Feito com bananas maduras e aveia, sem adição de açúcar refinado.', 12.00, 'banana.jpg'),
            ('Cupcake de Tâmara e Leite em Pó', 'Adoçado com pasta de tâmaras e recheio cremoso de leite em pó zero açúcar.', 15.00, 'tamara_leite.jpg')
        ]
        cursor.executemany('''
            INSERT INTO produtos (nome, descricao, preco, imagem_url) 
            VALUES (?, ?, ?, ?)
        ''', produtos_iniciais)
        conn.commit()
    conn.close()

# Inicializa o banco de dados ao subir o app
inicializar_bd()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return jsonify(produtos)
    except Exception as e:
        return jsonify({'erro': f'Falha na conexão: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)