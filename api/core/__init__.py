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

def create_app(config_path="./config.yml"):

    app = Flask("core")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    db_utils = DatabaseUtils(config["database"]["host"])
    db_utils.init_tables()

    allowed_origins = config["api"]["allowed_origins"]

        
    def build_get_response(object_name, object_id):
        response = {}
        msg = ""
        status = 500

        if type(object_id) is not int:
            msg = "Invalid value given for {} id".format(object_name)
        else:
            object_id = escape(object_id)
            results = db_utils.get(model_factory.tables["BOARD"], 
                model_factory.tables["BOARD"].board_id == board_id)
            
            try:
                for i in range(len(results)):
                    response[i] = results[i]
            except IndexError:
                msg = "No results found for given {} id".format(object_name)
            except KeyError:
                msg = "No results found for given {} id".format(object_name)

        response["status"] = status
        response["msg"] = msg
        response["board_name"] = board_name

        

    @app.route("/board/new", methods=["POST"])
    def create_board():

        json_data = json.loads(request.json)
        board_name = escape(json_data["board_name"])

        board = model_factory.create_model_object("BOARD")
        board.board_name = board_name

        result = db_utils.add(board)
        if result["result"] == True:
            result["status_code"] = 200
        else:
            result["status_code"] = 500
        result["result"] = None
        response = _create_response_object(result)
        return response

    @app.route("/board/<int:board_id>", methods=["GET"])
    def get_board(board_id):
        response = {}
        msg = ""
        board_name = ""
        status = 500

        if type(board_id) is not int:
            msg = "Invalid value for board id"
        else:
            board_id = escape(board_id)
            result = db_utils.get(model_factory.tables["BOARD"], 
                model_factory.tables["BOARD"].board_id == board_id)
            
            try:
                board_name = result[0].board_name
            except IndexError:
                msg = "No results found for given board id"
            except KeyError:
                msg = "No results found for given board id"

        response["status"] = status
        response["msg"] = msg
        response["board_name"] = board_name

        return _create_response_object(response)

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

