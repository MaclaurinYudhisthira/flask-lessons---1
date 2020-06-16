from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",fname="fname",lname="lname")

@app.route("/<fname>-<lname>")
def homear(fname,lname):
    return render_template("index.html",fname=fname,lname=lname)


if __name__=="__main__":
    print("==================Running==================")
    app.run()
    print("=================+++Off+++=================")