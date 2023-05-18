from flask import Flask, jsonify, request, current_app
from markupsafe import escape

import yaml
import json

from .dbengine import DatabaseUtils
from .modelfactory import ModelFactory

allowed_origins = None
db_utils = None
model_factory = ModelFactory()

def _create_response_object(data):
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", allowed_origins)
    return response

def _validate_input(input, is_integer_expected=True):
    if is_integer_expected and type(input) is not int:
        raise ValueError("Integer is expected")
    else:
        input = escape(input)
    return input

def create_app(config_path="./config.yml"):

    app = Flask("core")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    db_utils = DatabaseUtils(config["database"]["host"])
    db_utils.init_tables()

    allowed_origins = config["api"]["allowed_origins"]

    def _make_get_request(model, where):
        """
        model - the model class that extends DeclarativeBase
        where - premade where clause that should reference the same table as model
        """
        response = {
            "msg": "",
            "status": 200,
            "data": [],
        }

        
        result = db_utils.get(model, where)
        if len(result["errors"]) == 0:
            if len(result["rows"]) == 0:
                response["msg"] = "No results found for given input."
            else:
                for i in range(len(result["rows"])):
                    response["data"].append(result["rows"][i].to_dict())
        else:
            #Log the errors here
            for error in result["errors"]:
                print(error)
            response["status"] = 500
            response["msg"] = "An internal error occurred while processing the request."
        print(response)
        return _create_response_object(response)


    def _make_post_request(model, where):
        """
        model - the model class that extends DeclarativeBase
        where - premade where clause that should reference the same table as model
        """
        response = {
            "msg": "",
            "status": 200,
            "data": {},
        }

        try:
            rows = db_utils.get(model, where)
            if len(rows == 0):
                response["msg"] = "No results found for given input."
            else:
                response["data"] = rows
        except:
            response["status"] = 500
            response["msg"] = "An internal error occurred while processing the request."

        return _create_response_object(response)


    @app.route("/board/new", methods=["POST"])
    def create_board():

        json_data = json.loads(request.json)

        try:
            board_name = escape(json_data["board_name"])
        except KeyError:
            raise KeyError("No board name was given.")

        board = model_factory.create_model_object("BOARD")
        board.board_name = board_name

        result = db_utils.add(board)
        if result["result"] == True:
            result["status_code"] = 200
        else:
            result["status_code"] = 500
        result["result"] = None

        response = _create_response_object(result)
        print(result)
        return response

    @app.route("/board/<int:board_id>", methods=["GET"])
    def get_board(board_id):

        board_id = _validate_input(board_id)
        model = model_factory.tables["BOARD"]
        where = model.board_id == board_id

        response = _make_get_request(model, where)

        return response

    @app.route("/board/<int:boardId>/reply/<int:replyId>", methods=["GET"])
    def get_reply():
        reply = {}
        return _create_response_object(reply)

    @app.route("/board/<int:boardId>/thread/<int:threadId>/replies", methods=["GET"])
    def get_replies():
        """
        Get replies in a thread
        """
        replies = []
        return _create_response_object(replies)

    def create_reply():
        pass
    def delete_reply():
        pass

    @app.route("/board/<int:boardId>/thread/<int:threadId>", methods=["GET"])
    def get_thread():
        """
        Get a thread in a board
        """
        thread = { "test": "test"}
        return _create_response_object(thread)


    @app.route("/board/<int:boardid>/threads", methods=["GET"])
    def get_threads():
        """
        Get all threads in board
        """
        threads = []
        return _create_response_object(threads)

    def create_thread():
        pass
    def delete_thread():
        pass

    return app

