from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors={}
    if request.method == 'GET':
        return render_template('login.html', errors=errors)
    

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html', username=username)

    errors["cred"]= 'Неверные логин и/или пароль' 
    #username= request.args.get('username')
    print(f"pass = {password}")
    if username == '':
        errors['username']= 'Не введен логин!'
    if password == '':
        errors['password']= 'Не введен пароль!'
    return render_template('login.html', username=username, password=password, errors=errors)


@lab4.route('/lab4/success')
def order():
    return render_template('login.html')

