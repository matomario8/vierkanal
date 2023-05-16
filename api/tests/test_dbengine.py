import pytest
import yaml

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String

from core.dbengine import DatabaseUtils
from core.modelfactory import ModelFactory

class ModelTestBase(DeclarativeBase):
    pass

class ModelTest(ModelTestBase):
    __tablename__ = "test"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(50))

def test_db_utils(config):

    model_factory = ModelFactory(tables_config={"MODELTEST": ModelTest})

    db_utils = DatabaseUtils(config["test"]["database"]["host"])
    assert None is not db_utils.engine

    db_utils.init_tables(ModelTest)

    model_object = model_factory.create_model_object("MODELTEST")
    model_object.name = "testobj123"
    model_object.id = 1

    db_utils.add(model_object)

    model_class = model_factory.tables["MODELTEST"]
    queried_object = db_utils.get(model_class, model_class.name.in_(["testobj123"]))

    assert queried_object.name == model_object.name