from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <h1>Лабораторные работы по WEB-программированию</h1>
            <ol>
            <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a></li>
        
            </ol>
        </main>

        <footer>
        &copy; Андронова Софья Александровна, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html>
"""
@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <head>
        <title>Андронова Софья Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <main>
            <h1>web-сервер на flask</h1>
        
            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>
            <a href="http://127.0.0.1:5000/menu" target="_blank">Меню</a>
            <h2>Реализованные роуты</h2>
            <li><a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Кот на дубе</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/cats" target="_blank">Коты?</a></li>
        </main>

        <footer>
            &copy; Андрнова Софья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
    <link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1 
            </header>
            <h1>Дуб</h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <footer>
            &copy; Софья Андронова, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Андронова Софья Александровна</h1>
        <img src="''' +  url_for('static', filename='logo_ngtu.png') + '''">
        <footer>
            &copy; Софья Андронова, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>Python</h1>
            <div>
            Python — это язык программирования, который широко 
            используется в интернет-приложениях, разработке программного 
            обеспечения, науке о данных и машинном обучении (ML). 
            Разработчики используют Python, потому что он эффективен, 
            прост в изучении и работает на разных платформах. Программы 
            на языке Python можно скачать бесплатно, они совместимы со 
            всеми типами систем и повышают скорость разработки.
            </div>
            <h2>Где применяется Python?</h2>
            
            <li>Веб-разработка на стороне сервера</li>
            <li>Автоматизация с помощью скриптов Python</li>
            <li>Разработка программного обеспечения</li>
            <li>Автоматизация тестирования программного обеспечения</li>
            
        </main>
        
        <img src="''' +  url_for('static', filename='python.png') + '''">
        <footer>
            &copy; Софья Андронова, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/cats')
def cats():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Кто такие кошки и что им нужно от людей?</h1>
        <div>
        Раскрыта главная тайна кошек! Уже очень давно многих заботливых 
        хозяев остро беспокоит один вопрос - почему кошки ни в какую не хотят 
        точить свои коготки на когтеточках и даже самые изощрённые подобные 
        приспособления так и остаются нетронутыми? И сколько ни спрашивали об 
        этом самих котов, никто из них так в этом и не признался.
        </div>
        <div>
        Но зоологи раскрыли эту тайну, и теперь умалчивать об этом больше 
        нет смысла. Сейчас вы узнаете важную новость. Оказывается, что 
        коты вовсе не точат ногти, как думали люди, а ставят метки на 
        выбранных предметах, тем самым обозначая зону своего влияния.
        </div>
        <img src="''' +  url_for('static', filename='cat.jpg') + '''">
        <footer>
            &copy; Софья Андронова, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route('/lab2/example')
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

@app.route('/lab2/')
def lab2():   
    return render_template('lab2.html')

@app.route("/lab2/kartinki")
def kartinki():
    name = 'Софья Андронова'
    number_lab = '2'
    group = 'ФБИ-12'
    number_course = '3'

    return render_template('kartinki.html', name=name, number_lab=number_lab, group=group, number_course=number_course)