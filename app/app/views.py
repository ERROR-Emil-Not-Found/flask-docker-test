from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def hello():
    # This could also be returning an index.html

    with open("temp.txt", 'a+') as f:
        f.write("hello world\n")
    return 'Hello World!<br><br>try also: <a href="/foo">foo<a/>'


@views.route("/foo")
def foo():
    return "This has been edited off of the server and then moved onto it"
