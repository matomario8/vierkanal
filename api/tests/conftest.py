import pytest
import yaml
from flask import Flask, current_app

from core import create_app

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
    with open("./tests/configtest.yml") as config_file:
        config = yaml.safe_load(config_file)

    return config