from flask import Flask,render_template, redirect, url_for, request, session, flash
from datetime import timedelta


app=Flask(__name__)
app.secret_key="hs/#$$g.a53s/#$$g.a53S64"
app.permanent_session_lifetime=timedelta(days=0,minutes=5)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=="POST":
        session.permanent=True
        session['name']=request.form['name']
        flash('You have logged in Successfully','success')
        return redirect(url_for("user"))
    else:
        if 'name' in session:
            flash('You are already logged in','info')
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/user")
def user():
    if 'name' in session:
        return render_template("new.html",name=session['name'])
    else:
        flash('You are not logged in','info')
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear() # session.pop('name',None)
    flash('You have logged out successfully','info')
    return redirect(url_for("login"))

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)