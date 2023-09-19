from flask import Flask, render_template
import requests

app = Flask(__name__)
blogs_url = 'https://api.npoint.io/cc1ce630da617b10d7b5'


@app.route('/')
def home_page():
    json_blogs = requests.get(blogs_url).json()
    return render_template('index.html', blogs=json_blogs)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def single_post(post_id):
    return render_template('post.html', post=json_blogs[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
