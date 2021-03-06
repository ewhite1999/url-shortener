import random


def shorten_url(long_url):
    clean_url = long_url.replace('/', '')
    return ''.join(random.choice(clean_url) for _ in range(5))


def find_long_url(short_url, db):
    long_url = db.query.filter_by(short_url=short_url).first().long_url
    return long_url


def find_short_url(long_url, db):
    short_url = db.query.filter_by(long_url=long_url).first().short_url
    return short_url
