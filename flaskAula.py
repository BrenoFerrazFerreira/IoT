from flask import Flask, request
from datetime import date


app = Flask(__name__)
pagina = """
    <html>
        <head>
            <title>{titulo}</title>
        </head>
        <body>
            <h1>{titulo}</h1>
            {corpo}
        </body>
    </html>
    """
@app.route("/")

def inicio():
    corpo = """
        <form method='post' action='/idade'>
            Digite o ano que você nasceu: <br />
            <input type='text' name='ano_nasc' />
            <br><br>
            <input type='submit' value='Calcular' />
        </form>
        """
    return pagina.format(titulo = "Idade", corpo = corpo)
@app.route('/idade', methods = ["POST"])

def idade():
    ano_nasc = int(request.form['ano_nasc'])
    ano_atual = int(date.today().year)
    idade = ano_atual - ano_nasc
    corpo = "A sua idade é " + str(idade) + " anos."
    return pagina.format(titulo = "Cálculo da Idade", corpo = corpo)

if __name__ == '__main__':
    app.run(debug = True)
