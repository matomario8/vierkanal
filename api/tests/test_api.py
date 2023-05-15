import pytest

def test_hello_world(client):
    response = client.get("/")
    assert b"API version 0.1" in response.data

def test_create_board(client):
    json = '{"board_name": "test"}'
    response = client.post("/board/new", json=json)
    print(response.json)
    assert 200 == response.json["status_code"]