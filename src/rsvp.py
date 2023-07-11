from flask import Flask, render_template, request, url_for, flash, redirect
import csv
import uuid

app = Flask (__name__)

def addEvent(dataContent):
    with open('eventos.csv', 'a', newline="") as csvFileEvent:
        eventWriter = csv.writer(csvFileEvent)
        eventWriter.writerow(dataContent)
    csvFileEvent.close()

def addGuest(dataContent):
    with open('convidados.csv', 'a', newline="") as csvFileGuest:
        gestWriter = csv.writer(csvFileGuest)
        gestWriter.writerow(dataContent)
    csvFileGuest.close()

@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/cerimonial/event")
def eventos():
    return render_template("createEvent.html")
                           
@app.route("/cerimonial/createEvent", methods=['POST'])
def criateEvent():
    #Get vars posted from html form
    eventName = request.form["nomeEvento"]
    eventDate = request.form["dataEvento"]
    eventLocate = request.form["endEvento"]

    #Id Evento
    idEvent = str(uuid.uuid4())
    addEvent([idEvent, eventName, eventDate, eventLocate])
    return render_template("eventCreated.html", eventName=eventName, eventDate=eventDate, eventLocate=eventLocate, idEvent=idEvent)

@app.route("/guest/confirm/<idEvent>", methods=['POST'])
def confirmPresense(idEvent):
    guestName = request.form["nomeConvidado"]
    guestPhone = request.form["telefoneConvidado"]
    guestEmail = request.form["emailConvidado"]
    idGuest = str(uuid.uuid4())
    addGuest([idGuest, guestName, guestPhone, guestEmail, idEvent])
    return render_template("confirmed.html", guestName=guestName)

@app.route("/guest/confirm/<idi>")
def confirmaepresenca(idi):
    return render_template("confirmForm.html", idi2=idi)

@app.route("/cerimonial/listConfirmed/<idEvento>")
def listapresenca(idEvento):
    with open('convidados.csv', 'r', newline="") as arqEvento_csv:
        convidadoReader = csv.reader(arqEvento_csv)
        retorno = []
        for linha in convidadoReader:
            if linha[4] == idEvento:
                retorno.append(linha)
    arqEvento_csv.close()            
    return render_template("listConfirmed.html", lista = retorno)


                       
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)