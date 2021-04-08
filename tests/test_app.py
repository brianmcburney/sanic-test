import pytest
from sanic_testing import TestManager


from app.main import app

ROUTES = ["/", "/blueprint"]


@pytest.fixture(scope="session")
def setup():
    TestManager(app)


@pytest.fixture
def test_client():
    return app.test_client


@pytest.mark.parametrize("route", ROUTES)
def test_get(test_client, route):
    value = {"value": "a"}
    request, response = test_client.post(route, json=value)
    assert response.status == 200
    assert response.json == [value]

    request, response = test_client.get(route)
    assert response.status == 200
    assert response.json == [value]


def test_get_works(test_client):
    value = {"value": "a"}
    request, response = test_client.post("/post", json=value)
    assert response.status == 200
    assert response.json == [value]

    request, response = test_client.get("/")
    assert response.status == 200
    assert response.json == [value]


@pytest.mark.parametrize("route", ROUTES)
def test_post(test_client, route):
    value = {"value": "a"}
    request, response = test_client.post(route, json=value)
    assert response.status == 200
    assert response.json == [value]


@pytest.mark.parametrize("route", ROUTES)
def test_put(route):
    value = {"value": "a"}
    request, response = app.test_client.post(route, json=value)
    assert response.status == 200
    assert response.json == [value]

    request, response = app.test_client.put(route, json=value)
    assert response.status == 200
    assert response.json == [value, value]


@pytest.mark.parametrize("route", ROUTES)
def test_delete(route):
    value = {"value": "a"}
    request, response = app.test_client.post(route, json=value)
    assert response.status == 200
    assert response.json == [value]

    request, response = app.test_client.delete(route)
    assert response.status == 200
    assert response.json == []
