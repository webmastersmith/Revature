from urllib import response
from flask import Flask
import json

from app.app import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'<p>Hello, World!</p>'
    assert response.status_code == 200

def test_name_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/bryon'

    res = client.get(url)
    assert res.get_data() == b"<p>Hello, bryon!</p>"
    assert res.status_code == 200