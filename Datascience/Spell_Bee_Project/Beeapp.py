# Importin Libraries
import os
from flask import Flask, render_template, request, session
from flask_session import Session
from BeeDB import *
# Creating Flask application
app = Flask (__name__)
# Configuring Sqlite DB
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "SpellBee.db"))
app.config ['SQLALCHEMY_DATABASE_URI'] = database_file

 # Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

@app.route('/all')
def show_DB():
   return render_template('show_DB.html', BeeWords = Bee.query.all() )

def main():
      # Create tables based on each table definition in `models`
      db.create_all()

@app.route("/")
  def index():
      flights = BeeWord.query.all()
      return render_template("index.html", flights=flights)

  if __name__ == "__main__":
      # Allows for command line interaction with Flask application
      with app.app_context():
          main()

# @app.route('/Bee', methods = ['GET', 'POST'])
# def new():
#    if request.method == 'POST':
    #   if not request.form['name'] or not request.form['city'] or not request.form['addr']:
        #  flash('Please enter all the fields', 'error')
    #   else:
        #  student = students(request.form['name'], request.form['city'],
            # request.form['addr'], request.form['pin'])
        #  
        #  db.session.add(student)
        #  db.session.commit()
        #  flash('Record was successfully added')
        #  return redirect(url_for('show_all'))
#    return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)






