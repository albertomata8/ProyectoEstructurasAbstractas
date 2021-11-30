#!/usr/bin/env python

from ctypes import resize
from flask import Flask, render_template, flash
from flask import request

from flask import make_response, session, redirect
from flask.helpers import url_for

import src.forms as forms
from src.contrasenas import passw_manager
from src.correos import send_book_table, conf_email

app = Flask(__name__)
app.secret_key = "any random string"

resev_people = [{'value':'1 persona'}, {'value':'2 personas'}, {'value':'3 personas'}, {'value':'4 personas'}, {'value':'5 personas'}, {'value':'6 personas'}, {'value':'7 personas'}]
Horas = [{'hora':'4 pm'},{'hora':'5 pm'},{'hora':'6 pm'},{'hora':'7 pm'},{'hora':'8 pm'},{'hora':'9 pm'},{'hora':'10 pm'},]

@app.route('/')
def index():
    
    if 'username' in session:
        username = session['username']
        print("Usuario: ",username)
        return render_template("index.html",username=True, UserID=username, resev_people=resev_people, Horas=Horas)
    else:
        return render_template("index.html",username=False)

@app.route('/logout')
def logout():
    session.pop('username')
    flash("Ha finalizado sesión!")
    return redirect(url_for('index'))
    

@app.route('/mas')
def mas():
    return render_template("mas.html")

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)
    
    if request.method == 'POST' and login_form.validate():
        if manejador_contrasenas.comparar(login_form.username.data, login_form.password.data):
            # resp = make_response(render_template("index.html"))
            session['username'] = login_form.username.data
            flash("Ha iniciado sesión!")
            return redirect(url_for('index'))
        else:
            login_form.password.data = ""
    else:
        print("Datos no validos")

    return render_template("login_wtf.html", form=login_form)


@app.route('/register', methods=['GET','POST'])
def register():
    register_form = forms.RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate():
        print("Valido!")
        if register_form.password1.data == register_form.password2.data:
            if manejador_contrasenas.save_new(register_form.username.data, register_form.password1.data, register_form.name.data,register_form.apellido.data,register_form.email.data):
                print("registro exitoso!")
                resp = make_response(render_template("index.html"))
                resp.set_cookie('userID', register_form.username.data)
                session['username'] = register_form.username.data
                try:
                    conf_email(register_form.username.data, register_form.email.data)
                except:
                    print("Error en el correo")


                return redirect(url_for('index'))
            else:
                print("registro Falló!")
        else:
            print('Contraseñas no coinciden')
    else:
        print("No válido!")

    return render_template("register_form.html", form=register_form)



@app.route('/get_reservation', methods=['GET','POST'])
def get_reservation():
    usuario = session['username']
    people = request.form.get('people')
    hora = request.form.get('Hora_select')
    date = request.form.get('select_date')

    # print(manejador_contrasenas.get_email(session['username']))


    email = manejador_contrasenas.get_email(session['username'])

    send_book_table(usuario, people, date, hora, email)


    print(str(date))
    print(str(people))
    print(str(hora))
    return redirect(url_for('index'))


if __name__=='__main__':
    base = 'base/base.db'
    manejador_contrasenas = passw_manager(base)
    app.run(debug=True, port = 2000)
