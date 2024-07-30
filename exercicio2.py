from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao meu portfólio!"


@app.route('/livros')
def lista_livros():
    try:
        df = pd.read_csv('static/livros.csv')
        livros = df.to_dict(orient='records')
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        livros = []
    return render_template('lista.html', livros=livros)

app.run(debug=True)
