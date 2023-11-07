from flask import Blueprint, render_template, request
lab4 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5.html')

