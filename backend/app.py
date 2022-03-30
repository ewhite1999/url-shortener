
from http import server
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    server.run(debug=True)


class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(10), unique=True, nullable=False)
    short_url = db.Column(db.String(200), unique=True, nullable=False)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/urls', methods=['GET', 'POST'])
def urls_routes():
    if request.method == 'GET':
        urls = URLS.query.all()
        urlsList = [{'long_url': url.long_url, 'short_url': url.short_url}
                    for url in urls]
        return jsonify(urlsList), 200