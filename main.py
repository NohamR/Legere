from flask import Flask, render_template, request

app = Flask('app')

classes = [
  'Sentimental', 'Anticipation', 'Science-fiction', 'Aventure', 'Philosophie',
  'Policier', 'Apprentissage', 'Fable', 'Horreur', 'Espionnage', 'Biographie'
]

histoire = []

@app.route('/')
@app.route('/main')
def main():
  return render_template('main.html', classes=classes)

# partie histoire
@app.route('/liste')
def liste():
  global histoire
  return render_template('liste.html', liste=histoire)

@app.route('/ficheDepuisListe', methods=['POST'])
def ficheDepuisListe():
  hist = None
  for e in histoire:
    if e['nom'] == request.form["nom"]:
      hist = e
      break
  print(hist)
  return afficherFiche(hist)

@app.route('/fiche', methods=['POST'])
def fiche():
  dico = {key: value for key, value in request.form.items()}

  return afficherFiche(dico)
def afficherFiche(hist):
  return render_template('fiche.html', hist=hist)

@app.route('/nouvelle')
def nouvelle():
  return render_template('nouvelle.html', classes=classes)

@app.route('/ajouter', methods=['POST'])
def ajouter():
  global histoire
  dico = {}
  for key, value in request.form.items():
    dico[key] = value
  histoire += [dico]
  return afficherFiche(dico)

# partie /don (inactif)
# @app.route('/don')
# def don():
#   print('/don')
#   return render_template('don.html')

donneepaypal = []

# parie paypal
@app.route('/paypal')
def paypal():
  print('/paypal')
  return render_template('paypal.html')

@app.route('/listepaypal')
def listepaypal():
  global donneepaypal
  return render_template('listepaypal.html', liste2=donneepaypal)

@app.route('/ficheDepuisListepaypal', methods=['POST'])
def ficheDepuisListepaypal():
  account = None
  for e in donneepaypal:
    if e['nom'] == request.form["nom"]:
      account = e
      break
  print(account)
  return afficherPayPal(account)

@app.route('/infopaypal', methods=['POST'])
def infopaypal():
  dico2 = {key: value for key, value in request.form.items()}
  print('/infopaypal')
  return afficherPayPal(dico2)
def afficherPayPal(account):
  return render_template('infopaypal.html', account=account)

@app.route('/addinfopaypal', methods=['POST'])
def addinfopaypal():
  global donneepaypal
  dico2 = {}
  for key, value in request.form.items():
    dico2[key] = value
  donneepaypal += [dico2]
  print('//addinfopaypal')
  return afficherPayPal(dico2)


# partie erreur
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
  return render_template('405.html'), 405

@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

app.run(host='0.0.0.0', port=8080)