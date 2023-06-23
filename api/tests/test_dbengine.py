import pytest
import yaml

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy_serializer import SerializerMixin

from core.dbengine import DatabaseEngine, get_connection, init_database_engine
from core.modelfactory import ModelFactory

class ModelTestBase(DeclarativeBase, SerializerMixin):
    pass

class ModelTest(ModelTestBase):
    __tablename__ = "modeltest"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(50))

def test_database_queries(app):

    model_factory = ModelFactory({"MODELTEST": ModelTest})

    database = init_database_engine(app, ModelTestBase)
    assert None is not database.engine

    model_object_id = 1
    model_object_name = "testobj123"

    model_object_id2 = 2

    model_object = model_factory.create_model_object("MODELTEST")
    model_object2 = model_factory.create_model_object("MODELTEST")

    model_object.name = model_object_name
    model_object.id = model_object_id

    model_object2.name = model_object_name
    model_object2.id = model_object_id2

    result = database.add(model_object)
    assert False is not result["success"]

    result = database.add(model_object2)
    assert False is not result["success"]

    model_class = model_factory.tables["MODELTEST"]
    queried_objects = database.get(model_class, 
                        model_class.name.in_([model_object_name]))

    assert model_object_name == queried_objects["rows"][0].name
    assert model_object_name == queried_objects["rows"][1].name

    # Check that this isn't just evaluating to a boolean
    where_clause = model_class.id == 1
    queried_objects = database.get(model_class, where_clause)

    assert 1 == len(queried_objects["rows"])

def test_update(app):
    model_factory = ModelFactory({"MODELTEST": ModelTest})

    database = init_database_engine(app)

    model_object_id = 1
    model_object_name = "testobj123"

    model_object = model_factory.create_model_object("MODELTEST")
    model_object.name = model_object_name
    model_object.id = model_object_id

    result = database.add(model_object)
    assert False is not result["success"]

    model = model_factory.get("MODELTEST")
    new_model_object_name = "testobj321"

    database.update(model, model.name == model_object_name, name=new_model_object_name)
    assert False is not result["success"]

    queried_objects = database.get(model, model.name.in_([new_model_object_name]))
    assert "testobj321" == queried_objects["rows"][0].name