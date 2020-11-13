import pytest

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"Base action"


def test_v2(app, client):
    res = client.get('/v2')
    assert res.status_code == 200
    assert res.data == b"Second action"

def test_v7(app, client):
    res = client.get('/v7')
    assert res.status_code == 200
    assert res.data == b"Brichev T.U. INBO-01-17"