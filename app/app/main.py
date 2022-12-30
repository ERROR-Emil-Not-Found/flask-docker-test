from flask import Flask

app = Flask(__name__)

from . import views

def run():
    app.run(host="0.0.0.0", debug=True, port=80)

if __name__ == "__main__":
    run()
