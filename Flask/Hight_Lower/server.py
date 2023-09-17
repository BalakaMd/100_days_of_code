from flask import Flask
import random

random_number = random.randint(1, 10)
app = Flask(__name__)
print(random_number)


@app.route('/<int:number>')
def gues_number(number):
    if number == random_number:
        return f'<h1>You right!The number is {number}</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number > random_number:
        return f'<h1>No, it is too high. Try again</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h1>No, it is too low. Try again</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


@app.route('/')
def main_page():
    return "<h1>Try guess a number between 1 and 10</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
