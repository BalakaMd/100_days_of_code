from flask import Flask, render_template
from datetime import datetime as dt

app = Flask(__name__)


@app.route('/')
def home_page():
    current_year = dt.now().year
    return render_template('index.html', year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
