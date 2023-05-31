import pytest
import yaml
from flask import Flask, current_app

from core import create_app
from core.config import Config

test_config_path = "./tests/configtest.yml"

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def config():
    Config.register_config(test_config_path)
    return Config.get()