from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clave secreta para la sesión
DB_NAME = 'users.db'



def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT NOT NULL,
                       password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#!-Termina la base de datos--!

@app.route('/')
def index ():
    if 'username' in session:
        return f'Bienvenido, {session["username"]}!'
    else:
         return redirect('/indexCli.html')

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
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                       (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect('/')
        else:
            return 'Credenciales inválidas. Inténtalo de nuevo.'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True,port=5000)
    