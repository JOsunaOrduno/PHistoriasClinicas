import pymysql
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = config.HEX_SEC_KEY
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    _usuario = request.form['usuario']
    _password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE usuario = %s AND password = %s", (_usuario, _password))
    user = cur.fetchone()
    cur.close()

    if user is not None:
        return redirect(url_for('tasks'))
    else:
        return render_template('index.html', message="Las credenciales no son correctas")

@app.route('/tasks', methods=['GET'])
def tasks():
    
    return render_template('tasks.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))   
if __name__ == '__main__':
    app.run(debug=True)