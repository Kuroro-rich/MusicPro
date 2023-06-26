from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index ():
    return render_template('indexCli.html')

@app.route('/pedidos')
def pedidos ():
    return render_template('pedidosCli.html')

@app.route('/carro')
def carro ():
    return render_template('carroCli.html')

@app.route('/productos')
def productos ():
    return render_template('prodCli.html')

@app.route('/login')
def login ():
    return render_template('loginCli.html')

@app.route('/register')
def register ():
    return render_template('registerCli.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
    