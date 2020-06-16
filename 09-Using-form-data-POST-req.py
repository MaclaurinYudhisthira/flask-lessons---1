from flask import Flask,render_template, redirect, url_for, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=="POST":
        return redirect(url_for("new",name=request.form['name']))
    else:
        return render_template("login.html")

@app.route("/<name>")
def new(name):
    return render_template("new.html",name=name)

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)

    