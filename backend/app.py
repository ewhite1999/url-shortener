
from http import server
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import helpers
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    server.run(debug=True)


class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(200), unique=True, nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)


@app.route('/')
def home():
    return 'Hello, World!'


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
            # TODO: make this function
            short_url = helpers.shorten_url(long_url)
            # TODO: need to check if URL already in db first (try except block)
            newUrl = URLS(long_url=long_url, short_url=short_url)
            db.session.add(newUrl)
            db.session.commit()
            urlsList = {'long_url': long_url, 'short_url': short_url}

            return jsonify(urlsList), 201

        except exc.IntegrityError as err:
            db.session.rollback()
            errMessage = str(err.orig)
            if(errMessage == 'UNIQUE constraint failed: URLS.long_url'):
                # TODO: this catches what happens if they try to add a url we already have, make it so it returns the object
                return errMessage
            return 'oops something went wrong, please try again'


@app.route('/<url>')
def get_by_url(url):
    try:
        long_url = helpers.find_long_url(url, URLS)
        return(long_url), 200
    except AttributeError:
        # TODO: this needs to reroute them to the homepage
        return "We haven't made a url for that"
