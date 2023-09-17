from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return "<h1>Hello, World!</h1>"


@app.route('/<name>')
def gues_name(name):
    response_gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    response_age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    return render_template('index.html', person_name=name, age=response_age, gender=response_gender)

@app.route('/blog')
def blog():
    url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(url_blog).json()
    print(blog_response)
    return render_template('blog.html', blogs=blog_response)


if __name__ == "__main__":
    app.run(debug=True)
