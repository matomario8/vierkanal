from flask import g, current_app
from sqlalchemy import create_engine, Engine, select, update
from sqlalchemy.orm import Session

from models import *

db_engine = None

def init_database_engine(db_host, model=Base):
    db_engine = DatabaseEngine(db_host)
    db_engine.init_tables(model)

def get_connection():
    if "db_connection" not in g:
        g.db_connection = db_engine.create_connection()
    return g.db_connection

class DatabaseEngine:
    """Functions to initialize and run queries on the database"""

    engine: Engine

    def __init__(self, db_host: str):
        self.engine = create_engine(db_host, echo=True)

    def init_tables(self, model=Base):
        model.metadata.create_all(self.engine)
    
    def create_connection(self):
        return engine.connect()

    def add(self, model_object: DeclarativeBase) -> bool:
        """Adds an object of type DeclarativeBase to the db"""

        result = {
            "success": False, 
            "errors": []
        }

        # Put this into the log
        print("Adding the following to the db")
        print(model_object.to_dict())

        with Session(self.engine) as session:
            try:
                session.add(model_object)
                session.commit()
                result["success"] = True
            except:
                result["errors"].append("Could not add object into database.")
            
        return result

    def get(self, model, where=None):

        result = {
            "rows": [],
            "errors": []
        }

        with Session(self.engine) as session:
            try:
                stmt = select(model).where(where)
            except:
                result["errors"].append("Problem building the query.\
                                         SELECT: {} WHERE {}".format(model, where))
            try:
                for obj in session.scalars(stmt):
                    result["rows"].append(obj)
            except:
                result["errors"].append("Problem reading rows from database.")
        
        return result

    def update(self, model, where, **kwargs):
        result = {
            "success": False, 
            "errors": []
        }

        with Session(self.engine) as session:
            try:
                stmt = update(model).where(where).values(kwargs)

                session.execute(stmt)
                session.commit()
                result["success"] = True
            except:
                result["errors"].append("Unable to update object in database.")
        
        return result
            

            

