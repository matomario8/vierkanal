import pytest
import yaml

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String

from core.dbengine import DatabaseUtils
from core.modelfactory import ModelFactory

class ModelTestBase(DeclarativeBase):
    pass

class ModelTest(ModelTestBase):
    __tablename__ = "table"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(50))

def test_db_utils(config):

    model_factory = ModelFactory({"MODELTEST": ModelTest})

    db_utils = DatabaseUtils(config["database"]["host"])
    assert None is not db_utils.engine

    db_utils.init_tables(ModelTestBase)

    
    model_object_id = 1
    model_object_name = "testobj123"

    model_object = model_factory.create_model_object("MODELTEST")
    model_object.name = model_object_name
    model_object.id = model_object_id

    result = db_utils.add(model_object)

    assert False is not result["result"]

    model_class = model_factory.tables["MODELTEST"]
    
    queried_objects = db_utils.get(model_class, model_class.name.in_([model_object_name]))

    assert queried_objects.name == model_object_name


    #assert queried_object.name == model_object.name
