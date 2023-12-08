from flask import redirect, render_template, request, Blueprint 
import psycopg2

lab5 = Blueprint('lab5', __name__)


@lab5.route("/lab5")
def main():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_sofia",
        user="sofia_knowledge_base", 
        password="123")

    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return "go to console"

@lab5.route("/lab5/users")
def users():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_sofia",
        user="sofia_knowledge_base",
        password="123"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return render_template("users.html", result=result)