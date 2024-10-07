from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Portefeuilleelectronique',
    
    
 )
 

  




@app.route("/")
def login():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

#Bloc Gestion des utilisateurs

@app.route('/utilisateur')
def utilisateur():
    requete="SELECT *FROM utilisateur"
    curseur =db.cursor(buffered=True)
    curseur.execute(requete)
    utilisateur=curseur.fetchall()
    curseur.close()
    return render_template('utilisateur.html',utilisateur=utilisateur) 


@app.route('/enregistrer_utilisateur',methods=['POST','GET'])
def ajoute():
    if request.method == 'POST':
        requete ='INSERT INTO utilisateur (nom,email,telephone,mot_de_passe,date_creation) VALUES (%s,%s,%s,%s,%s)'
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        mot_de_passe = request.form['mot_de_passe']
        date_creation = request.form['date_creation']
        valeurs = (nom,email,telephone,mot_de_passe,date_creation)
        curseur = db.cursor()
        curseur.execute(requete, valeurs)
        db.commit()
        return redirect('/utilisateur')

@app.route("/ajoutUtilisateur")
def Form_AjoutUtilisateur():
    return render_template('ajoutUtilisateur.html')

   #modifUser 


@app.route('/modifier_utilisateur/<utilisateur_id>',methods=['POST','GET'])
def modifier_utilisateur(utilisateur_id):
    if request.method == 'POST':
        requete=('UPDATE utilisateur SET nom=%s,email=%s,telephone=%s,mot_de_passe=%s,date_creation=%s WHERE utilisateur_id=%s')
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        mot_de_passe = request.form['mot_de_passe']
        date_creation = request.form['date_creation']
        valeur = (nom,email,telephone,mot_de_passe,date_creation,utilisateur_id)
        curseur=db.cursor()
        curseur.execute(requete,valeur)
        
        return redirect('/utilisateur')
    


@app.route('/lancer_formmodification_utilisateur/<utilisateur_id>') 
def lancerUtil(utilisateur_id):
    requete='SELECT* FROM utilisateur WHERE utilisateur_id=%s'
    valeur=(utilisateur_id,)
    curseur=db.cursor()
    curseur.execute(requete,valeur)
    donnees=curseur.fetchall()
    return render_template('modifierUtilisateur.html',donnees=donnees)
 # Suppression
 
@app.route("/supprimer_utilisateur/<utilisateur_id>")
def supprimer_utilisateur(utilisateur_id):
    requete = ('DELETE from utilisateur WHERE utilisateur_id=%s')
    valeur = (utilisateur_id,)
    curseur = db.cursor()
    curseur.execute(requete,valeur)
    return redirect('/utilisateur')   
   
    
    #bloc creation compte
    
@app.route('/compte')
def compte():
    requete="SELECT *FROM compte"
    curseur =db.cursor(buffered=True)
    curseur.execute(requete)
    compte=curseur.fetchall()
    curseur.close()
    return render_template('compte.html',compte=compte)
    

@app.route('/enregistrer_compte',methods=['POST','GET'])
def ajouter():
    if request.method == 'POST':
        requete ='INSERT INTO compte (utilisateur_id,solde,type_compte,date_creation,statut) VALUES (%s,%s,%s,%s,%s)'
        utilisateur_id = request.form['utilisateur_id']
        solde = request.form['solde']
        type_compte = request.form['type_compte']
        date_creation = request.form['date_creation']
        statut = request.form['statut']
        valeurs = (utilisateur_id,solde,type_compte,date_creation,statut)
        curseur = db.cursor()
        curseur.execute(requete, valeurs)
        db.commit()
        return redirect('/compte')
    


@app.route("/ajoutCompte")
def Form_AjoutCompte():
    return render_template('ajoutCompte.html')


#modiFIER COMPTE

@app.route('/modifier_compte/<id>',methods=['POST','GET'])
def modifier_compte(id):
    if request.method == 'POST':
        requete=('UPDATE compte SET utilisateur_id=%s,solde=%s,type_compte=%s,date_creation=%s,statut=%s WHERE id=%s')
        utilisateur_id = request.form['utilisateur_id']
        solde = request.form['solde']
        type_compte = request.form['type_compte']
        date_creation = request.form['date_creation']
        statut = request.form['statut']
        valeur = (utilisateur_id,solde,type_compte,date_creation,statut,id)
        curseur=db.cursor()
        curseur.execute(requete,valeur)
        
        return redirect('/compte') 

@app.route('/lancer_formmodification_compte/<id>') 
def lancerCompte(id):
    requete='SELECT* FROM compte WHERE id=%s'
    valeur=(id,)
    curseur=db.cursor()
    curseur.execute(requete,valeur)
    donnees=curseur.fetchall()
    return render_template('modifierCompte.html',donnees=donnees)
    
    #supprimer compte
    
@app.route("/supprimer_compte/<id>")
def supprimer_compte(id):
    requete = ('DELETE from compte WHERE id=%s')
    valeur = (id,)
    curseur = db.cursor()
    curseur.execute(requete,valeur)
    return redirect('/compte')
    
    
    #Bloc pour les transactions 

@app.route('/transaction')
def transaction():
    requete="SELECT *FROM transaction"
    curseur =db.cursor(buffered=True)
    curseur.execute(requete)
    transaction=curseur.fetchall()
    curseur.close()
    return render_template('transaction.html',transaction=transaction)
    

@app.route('/enregistrer_transaction',methods=['POST','GET'])
def ajouteT():
    if request.method == 'POST':
        requete ='INSERT INTO transaction (compte_id,montant,type_transaction,date_transaction,description) VALUES (%s,%s,%s,%s,%s)'
        compte_id = request.form['compte_id']
        montant = request.form['montant']
        type_transaction = request.form['type_transaction']
        date_transaction = request.form['date_transaction']
        description = request.form['description']
        valeurs = (compte_id,montant,type_transaction,date_transaction,description)
        curseur = db.cursor()
        curseur.execute(requete, valeurs)
        db.commit()
        return redirect('/transaction')
    


@app.route("/ajoutTransaction")
def Form_AjoutTransaction():
    return render_template('ajoutTransaction.html')


#modifier trasaction

@app.route('/modifier_transaction/<id>',methods=['POST','GET'])
def modifier_transaction(id):
    if request.method == 'POST':
        requete=('UPDATE transaction SET compte_id=%s,montant=%s,type_transaction=%s,date_transaction=%s,description=%s WHERE id=%s')
        compte_id = request.form['compte_id']
        montant = request.form['montant']
        type_transaction = request.form['type_transaction']
        date_transaction = request.form['date_transaction']
        description = request.form['description']
        valeur = (compte_id,montant,type_transaction,date_transaction,description,id)
        curseur=db.cursor()
        curseur.execute(requete,valeur)
        
        return redirect('/transaction') 

@app.route('/lancer_formmodification_transaction/<id>') 
def lancerTransaction(id):
    requete='SELECT* FROM transaction WHERE id=%s'
    valeur=(id,)
    curseur=db.cursor()
    curseur.execute(requete,valeur)
    donnees=curseur.fetchall()
    return render_template('modifierTransaction.html',donnees=donnees)
    
    #supprimer la transaction
    
@app.route("/supprimer_transaction/<id>")
def supprimer_transaction(id):
    requete = ('DELETE from transaction WHERE id=%s')
    valeur = (id,)
    curseur = db.cursor()
    curseur.execute(requete,valeur)
    return redirect('/transaction')
    
#bloc pour les notifictions

@app.route('/notification')
def ajoutNotification():
    return render_template('notification.html') 

@app.route("/notification")
def listeNotifications():
    return render_template('notification.html')

@app.route('/enregistrer_notification',methods=['POST','GET'])
def ajouteN():
    if request.method == 'POST':
        requete ='INSERT INTO notification (utilisateur_id,message,date_envoi,statut,type_notification) VALUES (%s,%s,%s,%s,%s)'
        utilisateur_id = request.form['utilisateur_id']
        message = request.form['message']
        date_envoi = request.form['date_envoi']
        statut = request.form['statut']
        type_notification = request.form['type_notification']
        valeurs = (utilisateur_id,message,date_envoi,statut,type_notification)
        curseur = db.cursor()
        curseur.execute(requete, valeurs)
        db.commit()
        return redirect('/notification')

@app.route("/ajoutNotification")
def Form_AjoutNotification():
    return render_template('ajoutNotification.html')


@app.route('/afficherN')
def lancern():
    return render_template('ajoutNotification.html')

@app.route("/api/notifications", methods=["GET", "POST", "PUT", "DELETE"])
def apiNotifications():
    curseur = db.cursor(dictionary=True)
    if request.method == "GET":
        requete = "SELECT * FROM notification"
        curseur.execute(requete)
        donnees = curseur.fetchall()
        return jsonify(donnees)
    
    
    
    elif request.method == "DELETE":
        id = request.json['id']
        requete = "DELETE FROM notification WHERE id=%s"
        curseur.execute(requete, (id,))
        db.commit()
        return jsonify({"message": "Suppression réussie"})
    

 

if __name__=='__main__':
    app.run(debug=True)
   