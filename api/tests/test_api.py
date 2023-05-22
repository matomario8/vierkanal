import pytest
import json as jsonlib

def test_create_board(client):
    data = {
        "board_id": "g",
        "board_name": "technology"
    }
    json = jsonlib.dumps(data)
    response = client.post("/board/new", json=json)
    assert 200 == response.status_code

def test_get_board(client):
    data = {
        "board_id": "g",
        "board_name": "technology"
    }
    json = jsonlib.dumps(data)
    response = client.post("/board/new", json=json)
    assert 200 == response.status_code

    response = client.get("/board/g")
    assert 200 == response.status_code
    assert "g" == response.json["data"][0]["board_id"]
    assert "technology" == response.json["data"][0]["board_name"]

def test_create_thread(client):

    board_id = "t"
    board_name = "test"
    data = {
        "board_id": board_id,
        "board_name": board_name
    }
    json = jsonlib.dumps(data)
    url = "/board/new"
    response = client.post(url, json=json)
    assert 200 == response.status_code

    data = {
        "subject": "This is a thread",
        "author": "anonymous",
        "options": "sage",
        "comment": "Here's some more info about the thread",
    }
    json = jsonlib.dumps(data)

    url = "/board/" + board_name + "/newthread"
    
    response = client.post(url, json=json)
    assert 200 == response.status_code
    


def test_get_thread(client):
    pass


def test_create_reply(client):
    pass

def test_get_reply(client):
    pass