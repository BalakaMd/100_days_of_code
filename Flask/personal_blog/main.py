from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
json_blog = requests.get(url=blog_url).json()


@app.route('/')
def home():
    return render_template("index.html", blogs=json_blog)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template('post.html', post=json_blog[blog_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
