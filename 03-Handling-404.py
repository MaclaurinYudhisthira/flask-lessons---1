from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home page</h1>  <a href=\"/about\">About</a>"

@app.route("/about")
def about():
    return "<h1>About page</h1>  <a href=\"/\">Home</a>"

@app.errorhandler(404) 
def not_found(e): 

    return "<h1>404 Page not found</h1>"

if __name__=="__main__":
    print("==================Running==================")
    app.run()
    print("==================+++Off+++==================")