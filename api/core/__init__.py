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
    status_code = data["status_code"]
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", allowed_origins)
    return response, status_code

def _validate_input(input):
    return escape(input)

def create_app(config_path="./config.yml"):

    app = Flask("core")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    db_utils = DatabaseUtils(config["database"]["host"])
    db_utils.init_tables()

    allowed_origins = config["api"]["allowed_origins"]

    def _create_new_board_handler(board_id, board_name):
        board_object = model_factory.create_model_object("BOARD")
        board_object.board_id = board_id
        board_object.board_name = board_name
        db_utils.add(board_object)

        post_id_tracker_object = model_factory.create_model_object("POSTIDTRACKER")
        post_id_tracker_object.board_id = board_id
        post_id_tracker_object.next_post_id = 1
        db_utils.add(post_id_tracker_object)

    def _handle_get_request(model, where):
        """
        model - the model class that extends DeclarativeBase
        where - premade where clause that should reference the same table as model
        """
        response = {
            "msg": "",
            "status_code": 200,
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
            response["status_code"] = 500
            response["msg"] = "An internal error occurred while processing the request."

        return _create_response_object(response)

    def _handle_500(message):
        response = {
            "msg": message,
            "status_code": 200
        }
        return _create_response_object(response)
        

    def _handle_post_request(model):
        """
        model - the model class that extends DeclarativeBase
        """

        # Change to "data" for naming consistency with _create_response_object()
        response = {
            "msg": "",
            "status_code": 200
        }

        json_data = json.loads(request.json)

        model_object = model_factory.create_model_object(model)

        for key in json_data.keys():
            model_object.__dict__[key] = _validate_input(json_data[key])


        result = db_utils.add(model_object)
        if result["success"] == True:
            response["status_code"] = 200
        else:
            response["status_code"] = 500
            for error in result["errors"]:
                response["msg"] += error + "\n"

        return _create_response_object(response)


    @app.route("/board/new", methods=["POST"])
    def create_board():

        model = "BOARD"
        response = _handle_post_request(model)

        return response

    @app.route("/board/<string:board_id>", methods=["GET"])
    def get_board(board_id):

        board_id = _validate_input(board_id)
        model = model_factory.get("BOARD")
        where = model.board_id == board_id

        response = _handle_get_request(model, where)

        return response
    
    @app.route("/board/<int:board_id>/thread/<int:thread_id>/reply/new", methods=["POST"])
    def create_reply():
        model = "REPLY"
        response = _handle_post_request(model)
        return response

    @app.route("/board/<int:boardId>/reply/<int:replyId>", methods=["GET"])
    def get_reply():
        model = "REPLY"
        board_id = _validate_input(board_id)

        model = model_factory.tables["BOARD"]
        where = model.board_id == board_id

        response = _handle_get_request(model, where)

        return response

    @app.route("/board/<int:boardId>/thread/<int:threadId>/replies", methods=["GET"])
    def get_replies():
        """
        Get replies in a thread
        """
        replies = []
        return _create_response_object(replies)


    def delete_reply():
        pass

    @app.route("/board/<string:board_name>/thread/<int:threadId>", methods=["GET"])
    def get_thread():
        """
        Get a thread in a board
        """
        thread = { "test": "test"}
        return _create_response_object(thread)


    @app.route("/board/<string:board_name>/thread/getall", methods=["GET"])
    def get_threads():
        """
        Get all threads in board
        """
        threads = []
        return _create_response_object(threads)

    @app.route("/board/<string:board_id>/newthread", methods=["POST"])
    def create_thread(board_id):

        post_id_tracker = model_factory.get("POSTIDTRACKER")
        result = db_utils.get(post_id_tracker, post_id_tracker.board_id == board_id)

        if len(result["rows"]) == 0:
            message = ""
            for msg in result["errors"]:
                message += msg + "\n"
            response = _handle_500(message)
        else:
            next_post_id = result["rows"][0]["next_post_id"]
            result = db_utils.update(post_id_tracker, post_id_tracker.board_id == board_id, 
                                next_post_id=post_id_tracker.next_post_id + 1)
            if result["success"] is not False:
                json_data = json.loads(request.json)
                json_data["post_id"] = next_post_id

                model = "THREAD"
                response = _handle_post_request(model)
            else:
                message = ""
                for msg in result["errors"]:
                    message += msg + "\n"
                response = _handle_500(message)
        return response

    def delete_thread():
        pass

    @app.route("/board/<string:board_name>/getnextid", methods=["GET"])
    def get_next_post_id():
        next_post_id = 1
        return next_post_id

    def init_boards(boards=None) -> None:
        if boards is None:
            _create_new_board_handler("g", "Technology")
            _create_new_board_handler("sp", "Sports")
        else:
            for board in boards:
                _create_new_board_handler(board.board_id, board.board_name)

    return app

