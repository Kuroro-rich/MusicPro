from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy 


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

#!-Termina la base de datos--!

@app.route('/')
def index ():
        if 'username' in session:
            return f"Hola, {session['username']}!"
        return redirect('/login')

@app.route('/pedidos')
def pedidos ():
    return render_template('pedidosCli.html')

@app.route('/carro')
def carro ():
    return render_template('carroCli.html')

@app.route('/productos')
def productos ():
    return render_template('prodCli.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect('/')
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True,port=5000)
    