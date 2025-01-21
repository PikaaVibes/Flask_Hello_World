from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route('/home')
def accueil():
    return render_template('home.html')

@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices')
def exercices():
    return render_template('exercices.html') #Comm2

@app.route('/template_la_maison_a_chier')
def template():
    return render_template('template_la_maison_a_chier.html')
  


@app.route('/jeu_de_des')
def des():
    return render_template('jeu_de_des.html')
  
if __name__ == "__main__":
  app.run(debug=True)
