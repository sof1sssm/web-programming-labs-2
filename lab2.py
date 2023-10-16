from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name, number_lab, group, number_course = 'Софья Андронова', 2, 'ФБИ-12', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'author': 'Тургенев Иван', 'name': 'Ася', 'genre': 'Повесть', 'pages': 94},
        {'author': 'Робертс Нора', 'name': 'Яд бессмертия', 'genre': 'Детектив', 'pages': 384},
        {'author': 'Ремарк Эрих Мария', 'name': 'Триумфальная арка', 'genre': 'Роман', 'pages': 540},
        {'author': 'Дойл Артур Конан', 'name': 'Долина ужаса', 'genre': 'Детектив', 'pages': 608},
        {'author': 'Дойл Артур Конан', 'name': 'Знак четырех', 'genre': 'Детектив', 'pages': 192},
        {'author': 'Маринина Александра', 'name': 'Иллюзия греха', 'genre': 'Детектив', 'pages': 448},
        {'author': 'Ремарк Эрих Мария', 'name': 'Три товарища', 'genre': 'Роман', 'pages': 480},
        {'author': 'Гоголь Николай', 'name': 'Ревизор', 'genre': 'Комедия', 'pages': 192},
        {'author': 'Достоевский Фёдор', 'name': 'Преступление и наказание', 'genre': 'Роман', 'pages': 592},
        {'author': 'Пушкин Александр', 'name': 'Пиковая дама', 'genre': 'Повесть', 'pages': 224},
    ]
    return render_template('example.html', name=name, number_lab=number_lab, group=group, number_course=number_course, fruits=fruits, books=books)


@lab2.route("/lab2/")
def lab():   
    return render_template('lab2.html')


@lab2.route("/lab2/kartinki")
def kartinki():
    name = 'Софья Андронова'
    number_lab = '2'
    group = 'ФБИ-12'
    number_course = '3'

    return render_template('kartinki.html', name=name, number_lab=number_lab, group=group, number_course=number_course)