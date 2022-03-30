import json


class TestRoutes():
    def test_post_urls(self, api):
        mock_headers = {'Content-Type': 'application/json'}
        fakeData = json.dumps({
            "long_url": "https://pytest-flask.readthedocs.io/en/latest/tutorial.html"
        })
        respons = api.post('/urls', data=fakeData, headers=mock_headers)
        assert respons.status == '201 ADDED'
        assert len(respons.data) == 5
