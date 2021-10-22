import pytest

from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_google(client):
    result = client.get('/google')
    assert b'This is the google application' in result.data
    assert 200 == result.status_code


def test_host_routing_apple(client):
    result = client.get('/apple')
    assert b'This is the apple application' in result.data
    assert 200 == result.status_code


def test_host_routing_notfound(client):
    result = client.get('/notfound')
    assert b'Not found!' in result.data 
    assert 404 == result.status_code
