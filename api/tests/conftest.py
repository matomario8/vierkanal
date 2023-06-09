import pytest
import yaml
from flask import Flask, current_app

from core import create_app
from core.config import Config

test_config_path = "./tests/configtest.yml"

@pytest.fixture()
def app():
    app = create_app(test_config_path)
    app.config.update({"TESTING": True})
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

