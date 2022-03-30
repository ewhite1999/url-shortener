from http import server
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    server.run(debug=True)


class URLS(db.Model):
    long_url = db.Column(db.String(10), unique=True, nullable=False)
    short_url = db.Column(db.String(200), unique=True, nullable=False)


@app.route('/')
def home():
    return 'Hello, World!'
