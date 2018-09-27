import flask as flask
from flask import Flask
app = Flask(__name__)

@app.route("/createproject")
def createproject():
    return {project_id:"this is sample project id"}

if __name__ == "__main__":
    app.run()