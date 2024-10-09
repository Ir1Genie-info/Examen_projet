from flask import Flask ,render_template,request,redirect,url_for,session
import mysql.connector
from datetime import date
import mysql.connector
import os
import uuid
from flask_bcrypt import  Bcrypt
import secrets
from datetime import timedelta

db = mysql.connector.connect(
    host='localhost',
    username='muyisa',
    password='',
    database='location_appartement'
)
UPLOAD_FOLDER = 'static/uploads/'


cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Version de la base de données :", data)
db.close()




app= Flask(__name__)

db=mysql.connector.connect(
    database='location_appartement',
   user='muyisa',
     password='',
    host='localhost'
)

app.config['SECRET_KEY']= secrets.token_hex(16)
bcrypt=Bcrypt(app)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)


@app.route("/index")
def index():
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'
     req_C = 'SELECT COUNT(*)  FROM location WHERE DATEDIFF(fin,debut) < 30;'
     req_C = 'SELECT COUNT(*)  FROM location WHERE DATEDIFF(fin,NOW()) < 30;'
     req_Co = 'SELECT location.id,location.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom from location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client WHERE DATEDIFF(location.fin,NOW()) < 30 ;'     
     curseur = db.cursor(buffered=True)

     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()

     curseur.execute(req_C)
     nbnotif = curseur.fetchall()

     curseur.execute(req_Co)
     notif = curseur.fetchall()

     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')

     curseur.close()
     return render_template('index.html',commentaire=commentaire,nbmessage=nbmessage,firstname=firstname,lastname=lastname,image=image,role=role,nbnotif = nbnotif,notif=notif)



#les router pour  la table appartement
@app.route("/appartement")
def appartement():
     req = 'SELECT * FROM apartement;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()
     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()

     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')

     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('appartement.html',appartement=donnees,commentaire=commentaire,nbmessage=nbmessage,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image,role=role)

#L'ajout des appartement
@app.route("/enregistrer_apartement",methods=['POST','GET'])
def enregistrer_apartement():
    file = request.files['image']
    file2 = request.files['image2']
    idUp = request.form['idUp']
    nom = request.form['nom']
    prix = request.form['prix']
    detaille = request.form['detaille']
    adresse = request.form['addresse']
    categorie_appartement = request.form['categorie']
    chambre = request.form['chambre']
    superficie = request.form['superficie']
    status = 1
    if(idUp == ""):
         if file and file2:
          image_name = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
          image2_name = str(uuid.uuid4()) + os.path.splitext(file2.filename)[1]

          file.save(os.path.join(UPLOAD_FOLDER, image_name))
          file2.save(os.path.join(UPLOAD_FOLDER, image2_name))


          val = (nom,prix,detaille,adresse,categorie_appartement,image_name,status,superficie,chambre,image2_name)
          req = 'INSERT INTO `apartement`( `nom`, `prix`, `detaille`, `adrresse`, `categorie_appartement`, `image`, `status`,superficie,chambre,image2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          curseur = db.cursor()
          curseur.execute(req,val)
          db.commit()
          return redirect(url_for('appartement',status='sucsess',msg='enregistrement effectuer avec succès'))
    else:
         val = (nom,prix,detaille,adresse,categorie_appartement,image,idUp)
         if request.method == 'POST':
            req = 'UPDATE `apartement` SET `nom`=%s,`prix`=%s,`detaille`=%s,`adrresse`=%s,`categorie_appartement`=%s,`image`=%s WHERE id=%s'
            curseur = db.cursor()
            curseur.execute(req,val)
            db.commit()
            return redirect(url_for('appartement',status='sucsess',msg='La modification effectuer avec succès'))
@app.route("/suprimer_apartement",methods=['GET','POST'])
def suprimer_apartement():
     id = request.form['idDel']
     req = "DELETE FROM `apartement` WHERE id =%s"
     val = (id,)
     curseur = db.cursor()
     curseur.execute(req,val)
     return redirect(url_for('appartement',status='sucsess',msg='La suppression effectuer avec succès'))



#la route pour la table categorie-bien
@app.route("/categorie_apartement")
def categorie_apartement():
     req='SELECT * FROM categorie_appartement'
     curseur=db.cursor()
     curseur.execute(req)
     donnees=curseur.fetchall()
     status = request.args.get('status')
     msg = request.args.get('msg')
     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     return render_template('categorie_appartement.html',categorie_apartement=donnees,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image)

@app.route("/enregistrer_categorie_apartement",methods=['POST','GET'])
def enregistrer_categorie_apartement():
    
    description = request.form['description']
    idUp = request.form['idUp']
    status = 1
    if(idUp == ""):
     val = (description,)
     req = 'INSERT INTO `categorie_appartement`( `description`) VALUES (%s)'
     curseur = db.cursor()
     curseur.execute(req,val)
     db.commit()
     return redirect(url_for('categorie_apartement',status='sucsess',msg='Enregistrement effectuer avec succès'))
    else:
         val = (description,idUp)
         if request.method == 'POST':
            req = 'UPDATE `categorie_appartement` SET `description`=%s WHERE id=%s'
            curseur = db.cursor()
            curseur.execute(req,val)
            db.commit()
            return redirect(url_for('categorie_apartement',status='sucsess',msg='La modification effectuer avec succès'))
         
@app.route("/suprimer_categorie_apartement",methods=['POST','GET'])
def suprimer_categorie_apartement():
     id = request.form['idDel']
     req = "DELETE FROM `categorie_appartement` WHERE id =%s"
     val = (id,)
     curseur = db.cursor()
     curseur.execute(req,val)
     return redirect(url_for('categorie_apartement',status='sucsess',msg='La suppression effectuer avec succès'))


#Les routes pour le site
@app.route("/site_acceuil")
def site_acceuil():
     req = 'SELECT * FROM apartement;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 3'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()

     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.close()
     return render_template('site-acceuil.html',donnees = donnees,commentaire= commentaire)


#Les routes pour le site
@app.route("/appartement_site")
def appartement_site():
     req = 'SELECT * FROM apartement;'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()
     curseur.close()
     return render_template('appartement-site.html',donnees = donnees)

#La route pour commentater
@app.route('/commentaire',methods=['GET','POST'])
def commentaite():
     email = request.form['email']
     nom = request.form['nom']
     message = request.form['message']
     val = (nom,email,message)
     req = 'INSERT INTO commentaire (Nom,email,message,date) VALUE (%s,%s,%s,NOW())'
     curseur = db.cursor()
     curseur.execute(req,val)
     db.commit()
     return redirect('/site_acceuil')

#La route pour la reservation
@app.route('/reservation',methods=['GET','POST'])
def reservation():
     appartement = request.form['appartement']
     phone = request.form['phone']
     duree = request.form['duree']
     email = request.form['email']
     nom = request.form['nom']
     preuve = request.files['preuve']
     date_debut = request.form['datedebut']
     if preuve :
          image_name = str(uuid.uuid4()) + os.path.splitext(preuve.filename)[1]

          preuve.save(os.path.join(UPLOAD_FOLDER, image_name))
          val = (appartement,nom,email,phone,duree,image_name,date_debut,1)
          req = 'INSERT INTO reservation (date,appartement,nom,email,phone,duree,preuve,debut,lecture) VALUE (NOW(),%s,%s,%s,%s,%s,%s,%s,%s)'
          curseur = db.cursor()
          curseur.execute(req,val)
          db.commit()
          return redirect('/site_acceuil')
     
@app.route('/client')
def client():
     req = 'SELECT * FROM client;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()
     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()
     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')

     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('client.html',client=donnees,commentaire=commentaire,nbmessage=nbmessage,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image,role=role)


#L'ajout des Clients
@app.route("/enregistrer_client",methods=['POST','GET'])
def enregistrer_client():
    file = request.files['image']
    idUp = request.form['idUp']
    nom = request.form['nom']
    postnom = request.form['postom']
    prenom = request.form['prenom']
    etat = request.form['etat']
    phone = request.form['phone']
    status = 1
    if(idUp == ""):
         if file :
          image_name = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]

          file.save(os.path.join(UPLOAD_FOLDER, image_name))


          val = (nom,postnom,prenom,etat,phone,image_name,status)
          req = 'INSERT INTO `client`( `nom`, `postnom`, `prenom`, `etat_civil`, `phone`, `catre_electeur`, `status`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
          curseur = db.cursor()
          curseur.execute(req,val)
          db.commit()
          return redirect(url_for('client',status='sucsess',msg='enregistrement effectuer avec succès'))
    else:
         if request.method == 'POST':
            if file :
               image_name = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]

               file.save(os.path.join(UPLOAD_FOLDER, image_name))
               val = (nom,postnom,prenom,etat,phone,image_name,idUp)

               req = 'UPDATE `client` SET `nom`=%s,`postnom`=%s,`prenom`=%s,`etat_civil`=%s,`phone`=%s,`catre_electeur`=%s WHERE id=%s'
               curseur = db.cursor()
               curseur.execute(req,val)
               db.commit()
               return redirect(url_for('client',status='sucsess',msg='La modification effectuer avec succès'))

@app.route("/suprimer_client",methods=['POST','GET'])
def suprimer_categorie_client():
     id = request.form['idDel']
     req = "DELETE FROM `client` WHERE id =%s"
     val = (id,)
     curseur = db.cursor()
     curseur.execute(req,val)
     return redirect(url_for('client',status='sucsess',msg='La suppression effectuer avec succès'))

@app.route('/location')
def location():
     req = 'SELECT * FROM client;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'
     req3 = 'SELECT * FROM apartement;'
     req4 = 'SELECT location.id,location.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom from location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()
     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()

     curseur.execute(req3)
     appartement = curseur.fetchall()

     curseur.execute(req4)
     location = curseur.fetchall()
     

     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')
     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('location.html',client=donnees,commentaire=commentaire,nbmessage=nbmessage,appartement=appartement,location=location,status=status,msg=msg,image=image,firstname=firstname,role = role,lastname = lastname)


@app.route("/enregistrer_location",methods=['POST','GET'])
def enregistrer_location():
    idUp = request.form['idUp']
    appartement = request.form['appartement']
    client = request.form['client']
    debut = request.form['debut']
    fin = request.form['fin']
    status = 1
    if(idUp == ""): 
          val = (appartement,client,debut,fin,status)
          req = 'INSERT INTO `location`( `date`, `appartement`, `client`, `debut`, `fin`, `status`) VALUES (NOW(),%s,%s,%s,%s,%s)'
          curseur = db.cursor()
          curseur.execute(req,val)
          db.commit()
          return redirect(url_for('location',status='sucsess',msg='enregistrement effectuer avec succès'))
    else:
         if request.method == 'POST':
            
             val = (appartement,client,debut,fin,idUp)

             req = 'UPDATE `location` SET `appartement`=%s,`client`=%s,`debut`=%s,`fin`=%s WHERE id=%s'
             curseur = db.cursor()
             curseur.execute(req,val)
             db.commit()
             return redirect(url_for('location',status='sucsess',msg='La modification effectuer avec succès'))
         
@app.route("/supprimer_location",methods=['POST','GET'])
def suprimer_location():
     id = request.form['idDel']
     req = "DELETE FROM `location` WHERE id =%s"
     val = (id,)
     curseur = db.cursor()
     curseur.execute(req,val)
     return redirect(url_for('location',status='sucsess',msg='La suppression effectuer avec succès'))

#paiement
@app.route('/paiement')
def paiement():
     req = 'SELECT * FROM client;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'
     req3 = 'SELECT location.id,paiement.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom,paiement.location,paiement.montat,paiement.id from paiement JOIN location on location.id=paiement.location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client'
     req4 = 'SELECT location.id,location.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom from location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     donnees = curseur.fetchall()
     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()

     curseur.execute(req3)
     paiement = curseur.fetchall()

     curseur.execute(req4)
     location = curseur.fetchall()
     

     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')
     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('paiement.html',client=donnees,commentaire=commentaire,nbmessage=nbmessage,paiement=paiement,location=location,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image,role=role)


@app.route("/enregistrer_paiement",methods=['POST','GET'])
def enregistrer_paiement():
    idUp = request.form['idUp']
    location = request.form['location']
    montant = request.form['montant']
    status = 1
    if(idUp == ""): 
          val = (location,montant,status)
          req = 'INSERT INTO `paiement`( `date`, `location`, `montat`,status) VALUES (NOW(),%s,%s,%s)'
          curseur = db.cursor()
          curseur.execute(req,val)
          db.commit()
          return redirect(url_for('paiement',status='sucsess',msg='enregistrement effectuer avec succès'))
    else:
         if request.method == 'POST':
            
             val = (location,montant,idUp)

             req = 'UPDATE `paiement` SET `location`=%s,`montant`=%s WHERE id=%s'
             curseur = db.cursor()
             curseur.execute(req,val)
             db.commit()
             return redirect(url_for('paiement',status='sucsess',msg='La modification effectuer avec succès'))

@app.route("/supprimer_paiement",methods=['POST','GET'])
def suprimer_paiement():
     id = request.form['idDel']
     req = "DELETE FROM `paiement` WHERE id =%s"
     val = (id,)
     curseur = db.cursor()
     curseur.execute(req,val)
     return redirect(url_for('paiement',status='sucsess',msg='La suppression effectuer avec succès'))




@app.route('/utilisateur')
def utilisateur():
     req = 'SELECT * FROM users;'
     req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
     req2 = 'SELECT COUNT(*)  FROM commentaire;'
     req3 = 'SELECT location.id,paiement.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom,paiement.location,paiement.montat,paiement.id from paiement JOIN location on location.id=paiement.location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client'
     req4 = 'SELECT location.id,location.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom from location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client'

     curseur = db.cursor(buffered=True)

     curseur.execute(req)
     users = curseur.fetchall()
     curseur.execute(req1)
     commentaire = curseur.fetchall()

     curseur.execute(req2)
     nbmessage = curseur.fetchall()

     curseur.execute(req3)
     paiement = curseur.fetchall()

     curseur.execute(req4)
     location = curseur.fetchall()
     

     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')
     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('utilisateur.html',users=users,commentaire=commentaire,nbmessage=nbmessage,paiement=paiement,location=location,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image,role=role)

@app.route("/enregistrer_user", methods=['POST', 'GET'])
def enregistrer_user():
    idUp = request.form['idUp']
    nom = request.form.get('nom')
    postnom = request.form.get('postnom')
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    image = request.files['image']

    if idUp == "":
        if image:
            image_name = str(uuid.uuid4()) + os.path.splitext(image.filename)[1]
            image.save(os.path.join(UPLOAD_FOLDER, image_name))
            hash = bcrypt.generate_password_hash(password).decode('utf-8')
            val = (nom, postnom, username, hash, role, image_name)
            req = 'INSERT INTO `users`( `nom`, `postnom`, `username`, password, role, image) VALUES (%s, %s, %s, %s, %s, %s)'
            curseur = db.cursor()
            curseur.execute(req, val)
            db.commit()
            return redirect(url_for('utilisateur', status='success', msg='Enregistrement effectué avec succès'))
    else:
        req = 'UPDATE `users` SET '
        val = []
        if nom:
            req += '`nom`=%s, '
            val.append(nom)
        if postnom:
            req += '`postnom`=%s, '
            val.append(postnom)
        if username:
            req += '`username`=%s, '
            val.append(username)
        if password:
            hash = bcrypt.generate_password_hash(password).decode('utf-8')
            req += '`password`=%s, '
            val.append(hash)
        if role:
            req += '`role`=%s, '
            val.append(role)
        if image.filename != '':
            image_name = str(uuid.uuid4()) + os.path.splitext(image.filename)[1]
            image.save(os.path.join(UPLOAD_FOLDER, image_name))
            req += '`image`=%s, '
            val.append(image_name)
        
        # Remove the last comma and space
        req = req.rstrip(', ')
        req += ' WHERE `id`=%s'
        val.append(idUp)
        
        curseur = db.cursor()
        curseur.execute(req, tuple(val))
        db.commit()
        return redirect(url_for('login', status='success', msg='Mise à jour effectuée avec succès'))
         
@app.route('/')
def login():
     status = request.args.get('status')
     msg = request.args.get('msg')
     return render_template('connexion.html',status=status,msg=msg)

@app.route('/connexion', methods=['POST', 'GET'])
def connexion():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user is not None:
            pwdverif = bcrypt.check_password_hash(user[4], password)
            if pwdverif:
                session['loggedin'] = True
                session.permanent = True
                session['id'] = user[0]
                session['firstname'] = user[1]
                session['lastname'] = user[2]
                session['username'] = user[3]
                session['image'] = user[6]
                session['role'] = user[5]
                firstname = session.get('firstname')
                lastname = session.get('lastname')
                image = session.get('image')
                role = session.get('role')

                cursor = db.cursor(buffered=True)
                req1 = 'SELECT * FROM commentaire ORDER BY id DESC LIMIT 5;'
                req2 = 'SELECT COUNT(*) FROM commentaire;'
                req_C = 'SELECT COUNT(*)  FROM location WHERE DATEDIFF(fin,NOW()) < 30;'
                req_Co = 'SELECT location.id,location.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom from location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client WHERE DATEDIFF(location.fin,NOW()) < 30 ;'     
                cursor.execute(req1)
                commentaite = cursor.fetchall()

                cursor.execute(req2)
                nbmessage = cursor.fetchall()

                cursor.execute(req_C)
                nbnotif = cursor.fetchall()

                cursor.execute(req_Co)
                notif = cursor.fetchall()
                
                cursor.close()
                
                return render_template('index.html', firstname=firstname, lastname=lastname, username=username, image=image, commentaite=commentaite, nbmessage=nbmessage, role=role ,nbnotif = nbnotif,notif = notif)
        return redirect(url_for('login', status='echec', msg='Mot de passe ou username incorrect'))
    return redirect(url_for('login', status='echec', msg='Méthode non autorisée'))

@app.route('/deconnexion')
def deconnexion():
    session.clear()  # Efface toutes les données de session
    return redirect(url_for('login', status='success', msg='Vous avez été déconnecté avec succès'))

@app.route('/contact-site')
def contact_site():
     return render_template('contact.html')

@app.route('/profile')
def profile():
    firstname = session.get('firstname')
    lastname = session.get('lastname')
    image = session.get('image')
    role = session.get('role')
    id = session.get('id')
    username = session.get('username')
    return render_template('profile.html',lastname=lastname,firstname=firstname,image=image,role=role,id=id,username=username)

@app.route('/print_recu/<id>')
def print_recu(id):

     req = 'SELECT location.id,paiement.date,location.debut,location.fin,location.appartement,location.client,apartement.nom,client.nom,paiement.location,paiement.montat,paiement.id from paiement JOIN location on location.id=paiement.location JOIN apartement on apartement.id = location.appartement join client on client.id=location.client WHERE paiement.id = %s'

     val=(id,)
     curseur = db.cursor(buffered=True)
     curseur.execute(req,val)
     paiement = curseur.fetchall()
     

     curseur.close()
     status = request.args.get('status')
     msg = request.args.get('msg')
     firstname=session.get('firstname')
     lastname=session.get('lastname')
     image = session.get('image')
     role = session.get('role')
     return render_template('print_recu.html',paiement=paiement,location=location,status=status,msg=msg,firstname=firstname,lastname=lastname,image=image,role=role)


if __name__=='__main__':
   app.run(debug=True)