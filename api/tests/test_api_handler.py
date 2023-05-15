import pytest
from core.api_handler import *
from core.modelfactory import create_model_object, TABLES

def test_create_or_update_item():
    board_object = create_model_object("BOARD")
    board_object.board_name = "Test"

    # assert object doesn't exist
    #get_item(board_object)

    create_or_update_item(board_object)

    # assert item exists
    #get_item(board_object)