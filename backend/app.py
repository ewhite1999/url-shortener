from http import server
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import helpers

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)


class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(200), unique=True, nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)


@app.route('/')
def home():
    return 'Hello, World!', 200


@app.route('/urls', methods=['GET', 'POST'])
def urls_routes():
    # TODO: remove this before production
    if request.method == 'GET':
        urls = URLS.query.all()
        urlsList = [{'long_url': url.long_url, 'short_url': url.short_url}
                    for url in urls]

        return jsonify(urlsList), 200

    if request.method == 'POST':
        try:
            newData = request.json
            long_url = newData['long_url']
            short_url = helpers.shorten_url(long_url)
            newUrl = URLS(long_url=long_url, short_url=short_url)
            db.session.add(newUrl)
            db.session.commit()
            urlsList = {'long_url': long_url, 'short_url': short_url}

            return jsonify(urlsList), 201

        except exc.IntegrityError as err:
            db.session.rollback()
            errMessage = str(err.orig)

            if(errMessage == 'UNIQUE constraint failed: URLS.long_url'):
                prior_url = helpers.find_short_url(long_url, URLS)
                return jsonify({'message': 'We have already shortened that url!', 'long_url': long_url, 'short_url': prior_url}), 200

            return 'oops something went wrong, please try again', 500


@app.route('/<url>')
def get_by_url(url):
    try:
        long_url = helpers.find_long_url(url, URLS)
        return jsonify({'long_url': long_url}), 200

    except AttributeError:
        return jsonify({'message': 'We haven\'t made a url for that'}), 404


if __name__ == "__main__":
    server.run(debug=True)
