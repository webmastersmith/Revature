from flask import Flask

app = Flask(__name__)

def configure_routes(app):

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!!</p>"

    @app.route("/<name>")
    def hello_name(name):
        return "<p>Hello, " + name + "!</p>"
    
    @app.route("/goodbye/<name>")
    def goodbye_name(name):
        return "<p>Goodbye, " + name + "!</p>"

configure_routes(app)