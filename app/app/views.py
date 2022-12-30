
from .main import app
from os import getcwd


@app.route("/")
def hello():
    # This could also be returning an index.html

    with open("temp.txt", 'a+') as f:
        f.write("hello world\n")
    return 'Hello World!<br><br>try also: <a href="/foo">foo<a/>'


@app.route("/foo")
def foo():
    return "This has been added after the application was already running"
