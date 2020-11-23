from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

DATABASE = "./todo.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index")) #recharger la page après ajout d'une tâche, c'est implicit index.html
    #pass

@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() #chercher le todo dans la bdd
    todo.complete = not todo.complete 
    db.session.commit() #enregistrer
    return redirect(url_for("index")) #revenir sur page d'accueil
    #pass

@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
    #pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
