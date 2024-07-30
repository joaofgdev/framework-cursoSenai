from flask import Flask

app = Flask(__name__)


@app.route("/inicio")
def inicio():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site LGBT+</title>
    <style>
        /* Cores da bandeira LGBT+ */
        :root {
            --vermelho: #FF0000;
            --laranja: #FFA500;
            --amarelo: #FFFF00;
            --verde: #008000;
            --azul: #0000FF;
            --roxo: #800080;
        }

        /* Estilos gerais */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #FFFFFF;
        }

        header {
            background-color: var(--vermelho);
            color: #FFFFFF;
            padding: 1em;
            text-align: center;
        }

        nav {
            background-color: var(--laranja);
            padding: 1em;
            text-align: center;
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        nav li {
            display: inline-block;
            margin-right: 20px;
        }

        nav a {
            color: #FFFFFF;
            text-decoration: none;
        }

        main {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2em;
        }

        section {
            background-color: var(--amarelo);
            padding: 1em;
            margin-bottom: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: var(--verde);
        }

        p {
            color: var(--azul);
        }

        footer {
            background-color: var(--roxo);
            color: #FFFFFF;
            padding: 1em;
            text-align: center;
            clear: both;
        }
    </style>
</head>
<body>
    <header>
        <h1>Site LGBT+</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#">Início</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>
    <main>
        <section>
            <h1>Bem-vindo ao nosso site!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section>
            <h1>Nossa missão</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Site LGBT+. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

app.run()