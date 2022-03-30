from http import server
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    server.run(debug=True)


@app.route('/')
def home():
    return 'Hello, World!'
