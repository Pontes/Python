from flask import Flask, render_template

app = Flask(__name__)

@app.route('/apostilas')
def apostilas_online():
    lista_apostilas = ['HTML, CSS e Javascript', 'Java para Web', 'Flask', 'banco de dados']
    tam_lista = len(lista_apostilas)
    return render_template('apostilas.html', lista = lista_apostilas, qtd =tam_lista)

app.run()