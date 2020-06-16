from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home page</h1>"

if __name__=="__main__":
    
    print("==================Running==================")
    
    app.run()
    
    print("==================+++Off+++==================")