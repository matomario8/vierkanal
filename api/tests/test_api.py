import pytest
import json as jsonlib

THREAD = {
    "subject": "This is a thread",
    "author": "anonymous",
    "options": "sage",
    "comment": "Here's some more info about the thread"
}
THREAD_JSON = jsonlib.dumps(THREAD)

BOARD = {
    "board_id": "g",
    "board_name": "technology"
}
BOARD_JSON = jsonlib.dumps(BOARD)

def test_create_board(client):

    response = client.post("/board/new", json=BOARD_JSON)
    assert 200 == response.status_code

def test_get_board(client):

    response = client.post("/board/new", json=BOARD_JSON)
    assert 200 == response.status_code

    response = client.get("/board/g")
    assert 200 == response.status_code
    assert "g" == response.json["data"][0]["board_id"]
    assert "technology" == response.json["data"][0]["board_name"]

def test_create_thread(client):

    url = "/board/new"
    response = client.post(url, json=BOARD_JSON)
    assert 200 == response.status_code

    url = "/board/" + BOARD["board_name"] + "/newthread"
    
    response = client.post(url, json=THREAD_JSON)
    assert 200 == response.status_code
    


def test_get_thread(client):

    url = "/board/new"
    response = client.post(url, json=BOARD_JSON)
    assert 200 == response.status_code

    url = "/board/" + BOARD["board_name"] + "/newthread"
    response = client.post(url, json=THREAD_JSON)
    assert 200 == response.status_code

    post_id = "1"
    url = "/board/" + BOARD["board_name"] + "/thread/" + post_id
    response = client.get(url)
    assert 200 == response.status_code
    print(response.json["msg"])
    assert "This is a thread" == response.json["data"]

def test_get_thread_returns_invalid_input():
    
    pass

def test_create_reply(client):
    pass

def test_get_reply(client):
    pass