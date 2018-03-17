import os
from flask import Flask, render_template, flash, request,session, url_for, redirect
from module.database import Database

app = Flask(__name__)
app.secret_key = "super secret key"
DB_PATH = os.path.join(app.root_path, "database", "contact.db")


@app.route("/")
def index():
    db = Database(DB_PATH)
    data = db.read_all()
    return render_template("index.html",data=data)

@app.route("/add/")
def add():
    return render_template("add.html")


@app.route("/addcontact", methods=["POST", "GET"])
def addphone():
    if request.method == "POST" and request.form["save"]:
        data = {
            "Name": request.form["name"],
            "Phone": request.form["phone"],
            "Address": request.form["address"]
        }
        db = Database(DB_PATH)
        if db.insert(data):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/update/<int:id>/")
def update(id):
    db = Database(DB_PATH)
    row = db.read_by_id(id)
    if not row:
        return redirect(url_for("index"))
    else:
        session["update"] = id
        data = {
            "Name": row["Name"],
            "Phone": row["Phone"],
            "Address": row["Address"]
        }
        return render_template("update.html", data=data)


@app.route("/updatecontact", methods=["POST"])
def updatephone():
    if request.method == "POST" and request.form["update"]:
        db = Database(DB_PATH)
        data = {
            "Name": request.form["name"],
            "Phone": request.form["phone"],
            "Address": request.form["address"],
            "ContactId": int(session["update"])
        }
        if db.update(data):
            flash("A phone number has been updated")
        else:
            flash("A phone number can not be updated")
        session.pop("update", None)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/delete/<int:id>/")
def delete(id):
    db = Database(DB_PATH)
    row = db.read_by_id(id)
    print(row["Name"], row["Phone"], row["Address"])
    if not row:
        return redirect(url_for("index"))
    else:
        session["delete"] = id
        return render_template("delete.html", Name=row["Name"],
                               Phone=row["Phone"], Address=row["Address"])


@app.route("/deletecontact", methods=["POST"])
def deletephone():
    db = Database(DB_PATH)
    if request.method == "POST" and request.form["delete"]:
        if db.delete(session["delete"]):
            flash("A phone number has been deleted")
        else:
            flash("A phone number can not be deleted")
        session.pop("delete", None)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, port=8081)