import pytest

def test_create_board(client):
    json = '{"board_name": "test"}'
    response = client.post("/board/new", json=json)

    assert 200 == response.status_code

def test_get_board(client):
    json = '{"board_name": "test"}'
    client.post("/board/new", json=json)

    #insert a board then test
    response = client.get("/board/1")

    assert 200 == response.status_code
    assert "test" == response.json["board_name"]