from flask import Blueprint, redirect, url_for
lab1=Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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

        <h1>Лабораторные работы по WEB-программированию</h1>
        <menu>
        <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a></li>
        <li><a href="http://127.0.0.1:5000/lab2/" target="_blank">Лабораторная работа 2</a></li>
        <li><a href="http://127.0.0.1:5000/lab3/" target="_blank">Лабораторная работа 3</a></li>
        <li><a href="http://127.0.0.1:5000/lab4/" target="_blank">Лабораторная работа 4</a></li>
        </menu>
        <footer>
        &copy; Андронова Софья Александровна, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html>
"""


@lab1.route("/lab1/")
def lab():
    return """
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
"""


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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


@lab1.route('/lab1/python')
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


@lab1.route('/lab1/cats')
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


