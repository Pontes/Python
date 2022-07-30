from flask import Flask, render_template, request, redirect, session,flash

app = Flask(__name__)
app.secret_key = "pontes_ti_jr"

class Indica:
    def __init__(self, produto, categoria, empresa):
        self.produto = produto
        self.categoria = categoria
        self.empresa = empresa

loja1 = Indica('Criação de Site', 'tecnologia', 'PontesTI')
lista = [loja1]

@app.route('/')
def index():
    return render_template('lojas.html', titulo = "IndicaKI", lojas = lista)

@app.route('/cadastrar')
def novo():
    return render_template('cadastrar.html', titulo="Novas Ofertas")

@app.route('/criar', methods=['POST',])
def criar():
    produto = request.form['produto']
    categoria = request.form['categoria']
    empresa = request.form['empresa']
    indica = Indica(produto,categoria, empresa)
    lista.append(indica)
    return redirect('/')

@app.route('/logar')
def login():
    return render_template('logar.html')

@app.route('/autorizar', methods=['POST',])
def autorizar():
    if 'pwd' == request.form['password']:
        session['user_login'] = request.form['user']
        flash(request.form['user'] + ' User Authenticate.')
        return redirect('/')
    else:
        flash('User or Password is invalid! Try again')
        return redirect('/logar')

@app.route('/logout')
def logout():
    session['user_login'] = None
    flash("User Disconnected.")
    return redirect('/')


app.run(debug=True)