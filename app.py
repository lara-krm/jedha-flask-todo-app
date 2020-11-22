from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

DATABASE = "./todo.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


def add():
    pass


def complete(todo_id):
    pass


def delete(todo_id):
    pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
