from flask import Flask,render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="hs/#$$g.a53s/#$$g.a53S64"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.permanent_session_lifetime=timedelta(days=0,minutes=5)

db=SQLAlchemy(app)

class users(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    email=db.Column(db.String(100))

    def __init__(self,name,email):
        self.name=name
        self.email=email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=="POST":
        session.permanent=True
        session['name']=request.form['name']
        
        found_user=users.query.filter_by(name=session['name']).first()
        if found_user:
            session['email']=found_user.email
        else:
            user=users(request.form['name'],"")
            db.session.add(user)
            db.session.commit()

        flash('You have logged in Successfully','success')
        return redirect(url_for("user"))
    else:
        if 'name' in session:
            flash('You are already logged in','info')
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/user", methods=['POST','GET'])
def user():
    if 'name' in session:
        if request.method=="POST":
            session['email']=request.form['email']
            found_user=users.query.filter_by(name=session['name']).first()
            found_user.email=request.form['email']
            db.session.commit()
            flash("Email updated successfully")
        else:
            found_user=users.query.filter_by(name=session['name']).first()
            session['email']=found_user.email
        return render_template("user.html",data=[session['name'],session['email']])
    else:
        flash('You are not logged in','info')
        return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html",values=users.query.all())

@app.route("/logout")
def logout():
    # session.pop('name',None)
    session.clear()
    flash('You have logged out successfully','info')
    return redirect(url_for("login"))

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)