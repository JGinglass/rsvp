from flask import Flask, render_template, request, url_for, flash, redirect
import csv
import uuid

app = Flask (__name__)

def escrever_no_csv(dados):
    with open('eventos.csv', 'a', newline="") as arqEvento_csv:
        escritor_csv = csv.writer(arqEvento_csv)
        escritor_csv.writerow(dados)
    arqEvento_csv.close()

def gravar_convidado(dados):
    with open('convidados.csv', 'a', newline="") as arqEvento_csv:
        escritor_csv = csv.writer(arqEvento_csv)
        escritor_csv.writerow(dados)
    arqEvento_csv.close()

@app.route("/")
def homepage():
    return "<html><h2>Oi Joao</h2></html>"


@app.route("/eventos")
def eventos():
    return render_template("eventos.html")
                           
@app.route("/criaeventos", methods=['POST'])
def criaevento():
    nome = request.form["nomeEvento"]
    data = request.form["dataEvento"]
    ender = request.form["endEvento"]
    idi = str(uuid.uuid4())
    escrever_no_csv([idi, nome, data, ender])
    return render_template("link2.html", nome2=nome, data2=data, ender2=ender, idi2=idi)

@app.route("/confirmados/<idEvento>", methods=['POST'])
def confirmados(idEvento):
    nome = request.form["nomeConvidado"]
    tel = request.form["telefoneConvidado"]
    email = request.form["emailConvidado"]
    idi = str(uuid.uuid4())
    gravar_convidado([idi, nome, tel, email, idEvento])
    return render_template("link4.html", nome2=nome)

@app.route("/confirmapresenca/<idi>")
def confirmaepresenca(idi):
    return render_template("link3.html", idi2=idi)

@app.route("/listapresenca/<idEvento>")
def listapresenca(idEvento):
    with open('convidados.csv', 'r', newline="") as arqEvento_csv:
        convidadoReader = csv.reader(arqEvento_csv)
        retorno = []
        for linha in convidadoReader:
            if linha[4] == idEvento:
                retorno.append(linha)
    arqEvento_csv.close()            
    return render_template("link5.html", lista = retorno)


                       
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)