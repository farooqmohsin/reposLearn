from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = "farooq"
    return render_template("test.html", name=name)


if __name__ == '__main__':
    app.run()
