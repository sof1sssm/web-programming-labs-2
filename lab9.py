from flask import Blueprint, render_template, request

lab9= Blueprint('lab9', name)

@lab9.route('/lab9/')
def main():
        return render_template('lab9/index.html')


    