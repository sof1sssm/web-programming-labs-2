from flask import redirect, render_template, request, Blueprint 
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_sofia",
        user="sofia_knowledge_base", 
        password="123")
    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route("/lab5")
def main():
    visibleUser = "Anon"

    return render_template("lab5.html", username = visibleUser)

    # conn = dbConnect()
    # cur = conn.cursor()

    # cur.execute("SELECT * FROM users;")

    # result = cur.fetchall()

    # print(result)

    # dbClose(cur, conn)

    # return "go to console"


@lab5.route("/lab5/users")
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return render_template("users.html", result=result)

@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    # Если это метод GET, то верни шаблон и заверши выполнение 
    if request.method == "GET": 
        return render_template("register.html", errors=errors)

    # Если мы попали сюда, значит это метод РОЅT,
    # так как GЕT мы уже обработали и сделали return.
    # После return функция немедленно завершается 
    username = request.form.get("username") 
    password = request.form.get("password")

    # Провряем username и password на пустоту в 
    # Если любой из них пустой, то добавляем ошибку 
    # и рендерим шаблон
    if not (username or password): 
        errors.append("Пожалуйста, заполните все поля") 
        print(errors) 
        return render_template("register.html", errors=errors)

    # Если мы попали сюда, значит username и password заполненны
    # Подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()

    # Проверяем наличие клиента в базе
    # У нас не может быть два пользователя с одинаковыми логинами

    # WARNING: мы используем f-строки, что не рекомендуется делать 
    # позже мы разберемся с Вами почему не стоит так делать
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    # fetchone, a отличие, от fetchall, получает только одну строку 
    # мы задали свойство UNIQUE для пользователя, значит
    # больше одной строки мы не можем получить
    # Только один пользователь с таким именем может быть в БД
    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        dbClose(cur, conn) 
        return render_template("register.html", errors=errors)

    # Если мы попали сюда, то значит в cur.fetchone нет ни одной строки
    # значит пользователя с таким же логином не существует
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")

    # делаем commit - т.е. фиксируем изменения
    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")

