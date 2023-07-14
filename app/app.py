from flask import Flask, render_template, request, redirect, url_for, session, flash,jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re,os
from werkzeug.utils import secure_filename
from random import sample
from config import config

# from transbank.error.transbank_error import TransbankError
# from transbank.webpay.webpay_plus.transaction import Transaction

import random


app=Flask(__name__)
app.secret_key = 'key'

# webpay = Webpay("INTEGRATION", "NombreComercio", "CodigoComercio", "ApiKeyComercio", "ApiSecretComercio")

#configuracion de flask
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'
app.config['MAYSQL_PASSWORD']=''
app.config['MYSQL_DB']='productos'

# Configuración de la carga de archivos
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

#crear obj en bd
mysql=MySQL(app)

app.secret_key = 'mykey'

#rutas template
@app.route('/')
def index ():
    return render_template('register.html')

@app.route('/index')
def inicio ():
    return render_template('indexCli.html')


@app.route('/pedidos')
def pedidos ():
    return render_template('pedidosCli.html')



#eliminar
@app.route('/carro')
def carro ():
    return render_template('carroCli.html')




@app.route('/productos')
def productos():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM productos")
    datos = cur.fetchall()
    cur.close()
    return render_template('prodCli.html', productos=datos)




@app.route('/crudProd')
def crudProd ():
    return render_template('crudprodCLI.html')






#registro de usuario e inicio de sesion 

@app.route('/register', methods=['GET', 'POST'])
def register ():
    #output message de error
    msg = ''
    #Registro de usuario
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
       
        if account:
            msg = 'La cuenta ya existe!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'El correo ingresado no es valido!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'El nombre de usuario solo puede contener letras y números!'
        elif not username or not password or not email:
            msg = 'Por favor rellene el formulario!'
        else:
           
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (email,username, password,))
            mysql.connection.commit()
            msg = 'Se ha registrado exitosamente!'      
    # #Inicio de sesion
    # elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
    #     username = request.form['username']
    #     password = request.form['password']
   
    #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        
    #     account = cursor.fetchone()
    #     print('cuenta ingresada: ',account)
    #     if account:
    #         session['loggedin'] = True
    #         session['id'] = account['id']
    #         session['username'] = account['username']
    #         #return 'Ingresado exitosamente!'
    #         msg = "Ingresado exitosamente!"
    #         return render_template('indexCli.html', msg=msg)

    #     else:
            
    #         msg = 'Contraseña/Usuario incorrectos'
    
        

    elif request.method == 'POST':
        
        msg = 'Por favor rellene el formulario!'
    
    
    
        
    return render_template('register.html', msg=msg)




@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "En este endpoint se debe ejecutar un metodo POST"
    if request.method == 'POST':
        print('request.form: ')
        print(request.form) 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        print('cuentas: ',account)
        print('cuenta ingresada: ',account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            #return 'Ingresado exitosamente!'
            msg = "Ingresado exitosamente!"
            return render_template('indexCli.html', msg=msg)
        else:
            msg = 'Contraseña/Usuario incorrectos'
            return render_template('register.html', msg=msg)


@app.route('/login/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
   
    return redirect(url_for('indexCli.html'))




# Aleatoriedad de nombres, para evitar duplicidad de imágenes
def StringRandom():
    #Generar string random
    string_random = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
    len = 20
    secuencia = string_random.upper()
    resultado_random = sample(secuencia,len)
    string_random = "".join(resultado_random)
    return string_random




#ingresar productos
@app.route('/crudProd',methods=['GET','POST'])
def agregar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, nombre, precio, cantidad, categoria, SUBSTRING(foto, 1, LENGTH(foto) + 1) FROM productos')
    datos = cur.fetchall()
    
    if request.method == 'POST':
        #obtener datos formulario 
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
         # Cargar la foto y obtener la ruta
        foto = request.files['foto']
        filepath = os.path.dirname(__file__) #obtener ruta de archivo
        filename= secure_filename(foto.filename) #nombre archivo actual
        #capturar extensión/tipo de archivo
        tipo = os.path.splitext(filename)[1]
        new_name_file= StringRandom()+tipo
        subir_ruta=os.path.join(filepath,'static/uploads',new_name_file)
        foto.save(subir_ruta)
        
        #insertar nuevo prod
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, precio, cantidad, categoria, foto) VALUES (%s, %s, %s, %s, %s)',
                    (nombre, precio, cantidad, categoria, new_name_file.decode('utf-8')))
        
        mysql.connection.commit()
        flash('instrumento agregado')
        
        
        return redirect(url_for('agregar'))
    return render_template('crudprodCLI.html',productos=datos)




#editar producto
@app.route('/editar/<id>')
def get_instrumento(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s',(id))
    dato = cur.fetchall()
    return render_template('crudprodCLI.html',instrumento = dato[0])
#actualizar




@app.route('/actualizar/<int:id>',methods=['POST'])
def actualizar(id):
    if request.method =='POST':
        nombre= request.form['nombre']
        precio= request.form['precio']
        categoria= request.form['categoria']
        cantidad = request.form['cantidad']
        foto = request.files['foto']
        filepath = os.path.dirname(__file__) #obtener ruta de archivo
        filename= secure_filename(foto.filename) #nombre archivo actual
        #Capturar extensión de archivo (jpeg,jpg,etc.)
        tipo = os.path.splitext(filename)[1]
        new_name_file= StringRandom()+tipo
        subir_ruta=os.path.join(filepath,'static/uploads',new_name_file)
        foto.save(subir_ruta)
        
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE productos SET nombre=%s, precio=%s, cantidad=%s, categoria=%s, foto=%s WHERE id=%s",
                     (nombre, precio, cantidad, categoria, new_name_file ,id))
        mysql.connection.commit()
        
        flash('Instrumento actualizado ')
        return redirect(url_for('agregar'))
    
   
   
   
#eliminar pdoructo de la bd
@app.route('/eliminar/<int:id>')
def eliminar(id):
    # Eliminar el producto de la base de datos
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
        
    return redirect(url_for('agregar'))




def error_pagina_no_existe(error):
    return render_template('404.html'), 404





    
# Lógica para iniciar el pago y generar la URL de pago en Transbank
# @app.route('/pago', methods=['POST'])
# def iniciar_pago():
#     monto = request.args.get('monto')
#     orden_compra = 'ORDEN123'  # Genera un número de orden único
#     response = webpay.transaction.create(
#         amount=monto,
#         buy_order=orden_compra,
#         return_url='http://tudominio.com/callback'
#     )
#     return redirect(response['url'])



# @app.route('/callback', methods=['POST'])
# def callback_pago():
#     token_ws = request.form['token_ws']
#     response = webpay.transaction.commit(token_ws)
#     if response.response_code == 0:
#         # Pago exitoso, guardar en la base de datos, etc.
#         return 'OK'
#     else:
#         # Pago rechazado o fallido, manejar el error adecuadamente
#         return 'Error'


# @app.route("create", methods=["GET"])
# def webpay_plus_create():
#     monto=request.args.get('monto')
#     print("Webpay Plus Transaction.create")
#     buy_order = str(random.randrange(1000000, 99999999))
#     session_id = str(random.randrange(1000000, 99999999))
#     amount = monto
#     return_url = request.url_root + 'webpay-plus/commit'

#     create_request = {
#         "buy_order": buy_order,
#         "session_id": session_id,
#         "amount": amount,
#         "return_url": return_url
#     }

#     response = (Transaction()).create(buy_order, session_id, amount, return_url)

#     print(response)

#     return render_template('webpay/plus/create.html', request=create_request, response=response)


# @app.route("commit", methods=["GET"])
# def webpay_plus_commit():
#     token = request.args.get("token_ws")
#     print("commit for token_ws: {}".format(token))

#     response = (Transaction()).commit(token=token)
#     print("response: {}".format(response))

#     return render_template('webpay/plus/commit.html', token=token, response=response)

# @app.route("commit", methods=["POST"])
# def webpay_plus_commit_error():
#     token = request.form.get("token_ws")
#     print("commit error for token_ws: {}".format(token))

#     #response = Transaction.commit(token=token)
#     #print("response: {}".format(response))
#     response = {
#         "error": "Transacción con errores"
#     }

#     return render_template('webpay/plus/commit.html', token=token, response=response)    


# @app.route("refund", methods=["POST"])
# def webpay_plus_refund():
#     token = request.form.get("token_ws")
#     amount = request.form.get("amount")
#     print("refund for token_ws: {} by amount: {}".format(token, amount))

#     try:
#         response = (Transaction()).refund(token, amount)
#         print("response: {}".format(response))

#         return render_template("webpay/plus/refund.html", token=token, amount=amount, response=response)
#     except TransbankError as e:
#         print(e.message)


# @app.route("refund-form", methods=["GET"])
# def webpay_plus_refund_form():
#     return render_template("webpay/plus/refund-form.html")




if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,error_pagina_no_existe)
    app.run()