import random


def shorten_url(long_url):
    # TODO: Add some checking to make sure it hasn't randomly added the same url
    # TODO: rm special chars
    return ''.join(random.choice(long_url) for _ in range(5))
