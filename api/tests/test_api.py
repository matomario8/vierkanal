import pytest

def test_create_board(client):
    json = '{"board_name": "test"}'
    response = client.post("/board/new", json=json)

    assert 200 == response.status_code

def test_get_board(client):
    json = '{"board_name": "test"}'
    response = client.post("/board/new", json=json)

    assert 200 == response.status_code

    #insert a board then test
    response = client.get("/board/1")

    assert 200 == response.status_code

    assert "test" == response.json["data"][0]["board_name"]