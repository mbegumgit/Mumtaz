from flask import Flask, render_template, request, session
from flask_session import Session
import speakv1

app = Flask(__name__) # create new flask application with this file name

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
 
 

            
 
# Flask is designed in terms of route

@app.route("/sample")
def get_text():
    notes =['first', 'two','three']
    return render_template("test.html", notes=notes)

@app.route("/test", methods=["GET", "POST"])
def test():
     
    if request.method == "POST":
        if request.form.get("submit_pick"):
            level = request.form.get("level")
            if level:
                session['text'] = speakv1.SpeakWord(level)
                print('picked text:', session['text'])
                
            else:
                speakv1.CallEngine("select difficulty level to pick word")
                session['text']=" "
                print('exception A ',session['notes'])
            
        if request.form.get("submit_check"):
            typ_word = request.form.get("word")
            
            
            if session['text']:
                chk = speakv1.CheckWord(session['text'],typ_word)
                print('text:{}, chk status {}'.format(session['text'],type(chk)))
                dict_item ={typ_word:chk}
                session['notes'].append(dict_item)
            else:
                speakv1.CallEngine("select difficulty level to pick word")
                session['text'] = " "
    else:
        session['notes'] = []
        session['text']=''
         
    return render_template("test.html", notes=session['notes'])

@app.route("/test", methods=["GET", "POST"])
def check_word(text):
    if request.method == "POST":
        typ_word = request.form.get("word")
        chk = Sp.CheckWord(text,typ_word)
        if chk:
            notes.append(typ_word+" correct")
            #notes.append(note)
        else:
            notes.append(typ_word+" Incorrect")
            #notes.append(note)

if __name__ == '__main__':
    app.run(debug=True)