from flask import Blueprint, render_template, request

lab9= Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
        return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return "Нет такой страницы", 404


    