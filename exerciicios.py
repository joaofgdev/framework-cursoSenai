# Importa a biblioteca Flask, que é um framework para criar aplicações web em Python
from flask import Flask, render_template

# Importa a biblioteca Pandas, que é usada para manipular dados em Python
import pandas as pd

# Cria uma instância da classe Flask, que é a aplicação web em si
app = Flask(__name__)

# Define uma rota para a página inicial da aplicação
@app.route('/')
def home():
    # Retorna uma mensagem de boas-vindas para a página inicial
    return "Bem-vindo ao meu portfólio!"

# Define uma rota para a página de lista de livros
@app.route('/livros')
def lista_livros():
    try:
        # Tenta ler o arquivo CSV 'livros.csv' localizado na pasta 'static'
        df = pd.read_csv('static/livros.csv')
        
        # Converte o DataFrame (df) em um dicionário de registros (orient='records')
        livros = df.to_dict(orient='records')
    except Exception as e:
        # Se ocorrer um erro ao ler o arquivo CSV, imprime o erro e define a lista de livros como vazia
        print(f"Erro ao ler o arquivo CSV: {e}")
        livros = []
    
    # Retorna a renderização do template 'lista.html' com a lista de livros como parâmetro
    return render_template('lista.html', livros=livros)

# Executa a aplicação em modo de depuração (debug=True)
app.run(debug=True)