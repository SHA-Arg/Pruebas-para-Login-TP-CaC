from flask import Flask, render_template, request, redirect, url_for
from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()


# PRIMER INTENTO DE CONEXION A BASE DE DATOS

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_HOST'] = 'localhost'

# mysql = MySQL()


# @app.route('/', methods=['GET'])
# def login():
#     return render_template('login.html')


# @app.route('/add_user')
# def add_user():
#     return 'Add user page'


# @app.route('/edit_user')
# def edit_user():
#     return 'Edit user page'


# @app.route('/delete_user')
# def delete_user():
#     return 'Delete user page'


# if __name__ == '__main__':
#     app.run(debug=True)
