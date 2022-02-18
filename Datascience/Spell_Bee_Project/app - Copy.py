from flask import Flask, render_template, request, session
from flask_session import Session
import speak

app = Flask(__name__) # create new flask application with this file name

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

# Flask is designed in terms of route
@app.route("/", methods=["GET", "POST"])
def index():
    if session.get('notes') is None:
	    session['notes'] = []

    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)
        #notes.append(note)

    return render_template("index.html", notes=session['notes'])

@app.route('/new/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return 'Please submit the form!!'
	else:
		name = request.form.get('name')
		return render_template('hello.html', name=name)

@app.route("/spell", methods=["GET", "POST"])
def spell():
    level ='ONE'
    if session.get('notes') is None:
         
	    session['notes'] = []
        

    if request.method == "POST":
        typ_word = request.form.get("word")
        level = request.form.get("level")
        text = speak.SpeakWord(level)
        chk = speak.CheckWord(text,typ_word)
        if chk:
            session['notes'].append(typ_word+" correct")
            #notes.append(note)
        else:
            session['notes'].append(typ_word+" Incorrect")
            #notes.append(note)
         
    return render_template("spell.html", notes=session['notes'])

app.route("/spelltest", methods=["GET", "POST"])
def spelltest():
    level ='ONE'
    if request.method == "POST":
        typ_word = request.form.get("word")
        level = request.form.get("level")
        text = speak.SpeakWord(level)
        chk = speak.CheckWord(text,typ_word)
        if chk:
            notes.append(typ_word+" correct")
            #notes.append(note)
        else:
            notes.append(typ_word+" Incorrect")
            #notes.append(note)
    return render_template("spelltest.html", notes)

if __name__ == '__main__':
    app.run(debug=True)