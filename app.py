from flask import Flask, render_template, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'loja_cupcakes.db'

def init_db():
    """Inicializa o banco de dados e insere os produtos padrão."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            imagem_url TEXT NOT NULL
        )
    ''')
    
    # Verifica se a tabela está vazia para inserir os produtos
    cursor.execute('SELECT COUNT(*) FROM produtos')
    count = cursor.fetchone()[0]
    
    if count == 0:
        produtos_iniciais = [
            ('Cupcake de Maçã com Canela', 'Massa fofinha adoçada 100% com purê de maçã natural e um toque de canela.', 13.50, 'maca.png'),
            ('Cupcake de Banana com Aveia', 'Feito com bananas maduras e aveia, sem adição de açúcar refinado.', 12.00, 'banana.png'),
            ('Cupcake de Tâmara e Leite em Pó', 'Adoçado com pasta de tâmaras e recheio cremoso de leite em pó zero açúcar.', 15.00, 'banana.png')
        ]
        
        cursor.executemany('''
            INSERT INTO produtos (nome, descricao, preco, imagem_url)
            VALUES (?, ?, ?, ?)
        ''', produtos_iniciais)
        
        conn.commit()
    
    conn.close()

# Executa a inicialização do banco ao carregar a aplicação no servidor
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM produtos')
    linhas = cursor.fetchall()
    conn.close()
    
    produtos = []
    for linha in linhas:
        produtos.append({
            'id': linha['id'],
            'nome': linha['nome'],
            'descricao': linha['descricao'],
            'preco': linha['preco'],
            'imagem_url': linha['imagem_url']
        })
        
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)