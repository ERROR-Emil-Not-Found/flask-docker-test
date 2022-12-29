from ..api import api  # noqa
from ..main import app
from os import getcwd


@app.route("/")
def hello():
    # This could also be returning an index.html

    with open("temp.txt", 'a+') as f:
        f.write("hello world\n")
    return f"""Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template), 
     try also: <a href="/users/">/users/</a>
     
     current working directory: {getcwd()}"""
