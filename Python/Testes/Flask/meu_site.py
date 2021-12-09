# importação do Flask
from flask import Flask, render_template

# método necessário para inicialização do Flask
app = Flask(__name__)

# criar a página inicial (estática)
@app.route('/')
def paginainicial():
    return render_template('index.html')

# criar a página de usuário (dinâmica)
@app.route('/user/<name>')
def paginausuario(name):
    return render_template('user.html', name=name)















# colocar o site no ar:
if __name__ == '__main__':
    app.run(debug=True)
