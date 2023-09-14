from flask import Flask
import os

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        text = function()
        new_text = f'<b>{text}<b>'
        return new_text

    return wrapper_function


@app.route('/')
@make_bold
def hello_word():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
