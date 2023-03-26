# Copyright 2022 Youenn Pierre-Justin PIEY78070308
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, g, request, redirect, url_for
from database import Database
import random

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

def recherche_animaux(champ):
  base = get_db()
  list_animaux = []
  size = get_db().get_database_size() + 1
  for i in range(1, size):
    animal = base.get_animal(i)
    nom = animal['nom']
    desc = animal['description']
    ville = animal['ville']
    #Checker sans tenir compte de la case si le nom correspond
    if champ.lower() in nom.lower() or champ.lower() in desc.lower() or champ.lower() in ville.lower():
        list_animaux.append(animal)
  print(list_animaux)
  return list_animaux

def recherche_nom_animaux(champ):
  base = get_db()
  id = 0
  size = get_db().get_database_size() + 1
  for i in range(1, size):
    animal = base.get_animal(i)
    nom = animal['nom']
    testid = animal['id']
    #Checker sans tenir compte de la case si le nom correspond
    if champ.lower() in nom.lower():
        id=testid
  return id

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.route('/')
def accueil():
    animaux_list = []
    deja_pris = []
    animals=get_db()
    size = get_db().get_database_size()
    print(size)
    for i in range (5):
        r = random.randint(1,size)
        #Si l'animal est deja afficher on le change
        while r  in deja_pris:
            r = random.randint(1, size)
        deja_pris.append(r)
        animaux_list.append(animals.get_animal(r))
    print(animaux_list) #A SUPPRIMER
    return render_template('accueil.html', animaux_list=animaux_list)

@app.route('/adoption')
def adoption():
    return render_template('adoption.html')

@app.route('/search')
def search():
  recherche = request.args.get('recherche')
  # Search your database or other data source for the query
  results = recherche_animaux(recherche)
  return render_template('recherche.html', results=results)

@app.errorhandler(404)
def erreur(e):
    return render_template('404.html'), 404

@app.route('/soumettre', methods=['POST'])
def soumettre():

  erreur=0

  erreurnom = ""
  erreurespece = ""
  erreurrace = ""
  erreurage = ""
  erreurdescription = ""
  erreuremail = ""
  erreurrue = ""
  erreurville = ""
  erreurcodePostal = ""
  
  # Get the form data
  nom = request.form['nom']
  espece = request.form['espece']
  race = request.form['race']
  age = request.form['age']
  description = request.form['description']
  email = request.form['email']
  rue = request.form['rue']
  ville = request.form['ville']
  codePostal = request.form['code_postal']

  # Validate the form data
  if "," in nom:
    erreurnom = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not nom:
    erreurnom = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in espece:
    erreurespece = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not espece:
    erreurespece = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in race:
    erreurrace = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not race:
    erreurrace = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in age:
    erreurage = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not age:
    erreurage = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in description:
    erreurdescription = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not description:
    erreurdescription = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in email:
    erreuremail = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not email:
    erreuremail = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in rue:
    erreurrue = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not rue:
    erreurrue = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in ville:
    erreurville = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not ville:
    erreurville = "Le champ doit etre non nul"
    erreur += 1
    
  if "," in codePostal:
    erreurcodePostal = "Le champ ne doit pas contenir de virgule"
    erreur += 1
  if not codePostal:
    erreurcodePostal = "Le champ doit etre non nul"
    erreur += 1

  if erreur != 0:
    return render_template("adoption.html", submitErreur="Plusieurs champs sont invalides",
    nomErreur=erreurnom , especeErreur=erreurespece , raceErreur=erreurrace , ageErreur=erreurage , descriptionErreur=erreurdescription , 
    emailErreur=erreuremail , rueErreur= erreurrue, villeErreur= erreurville, code_postalErreur= erreurcodePostal, nom=nom , espece=espece , race=race ,
     age=age , description=description, email= email, rue= rue, ville= ville, code_postal= codePostal,)

  # Save the form data to a database or file
  animaux = get_db()
  animaux.add_animal(nom, espece,race,age,description,email,rue,ville,codePostal)

  # Redirect to the success page
  return redirect('/merci')

@app.route('/merci')
def success():
  animaux = get_db()
  size = get_db().get_database_size()
  nom = animaux.get_animal(size)['nom']
  return render_template('merci.html', nom=nom), 200, {'Refresh': '10; url=%s' % url_for('show_animal', name = nom)}

@app.route('/animal/<name>')
def show_animal(name):
    animaux = get_db()
    if recherche_nom_animaux(name) != 0:
        return render_template('animal.html', animal=animaux.get_animal(recherche_nom_animaux(name)))
    else:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
