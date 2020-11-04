import pytest

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"Base action"


def test_v2(app, client):
    res = client.get('/v2')
    assert res.status_code == 200
    assert res.data == b"Second action"

    def test_Sivashova(app, client):
    res = client.get('/Sivashova')
    assert res.status_code == 200
    assert res.data == b"Sivashova_Lyudmila INBO_01_17"