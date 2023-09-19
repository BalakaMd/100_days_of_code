from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['post', 'GET'])
def login():
    if request.method == 'post':
        name = request.form['name']
        password = request.form['password']
        return f"Name {name}, Password: {password}"
    else:
        return "Name: , Password: {password}"


if __name__ == '__main__':
    app.run(debug=True)
