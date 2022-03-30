import json


class TestRoutes():

    def test_get_urls(self, api):
        res = api.get('/urls')
        assert b"short_url" in res.data
        assert b"long_url" in res.data

    def test_post_urls(self, api):
        mock_headers = {'Content-Type': 'application/json'}
        fakeData = json.dumps({
            "long_url": "https://pytest-flask.readthedocs.io/en/latest/tutorial.html"
        })
        res = api.post('/urls', data=fakeData, headers=mock_headers)
        assert res.status == '200 OK'

    def test_home_route(self, api):
        res = api.get('/')
        assert res.data == b'Hello, World!'
        assert res.status == '200 OK'

    def test_get_by_url(self, api):
        res = api.get('/oh_no')
        assert b"We haven\'t made a url for that" in res.data
