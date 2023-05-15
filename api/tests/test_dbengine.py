import pytest
import yaml

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String

from core.dbengine import DatabaseUtils

class ModelTestBase(DeclarativeBase):
    pass

class ModelTest(ModelTestBase):
    __tablename__ = "test"

    test_id: Mapped[int] = mapped_column(primary_key=True)
    test_name: Mapped[str] = mapped_column(String(50))

def test_db_utils(config):


    db_utils = DatabaseUtils(config["test"]["database"]["host"])
    assert None is not db_utils.engine

    db_utils.init_tables(ModelTest)
    # run add and select functions