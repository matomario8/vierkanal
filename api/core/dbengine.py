from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session

from .models import *

class DatabaseUtils:

    engine: Engine

    def __init__(self, dbhost: str):
        self.engine = create_engine(dbhost, echo=True)

    def init_tables(self, model=Base):
        model.metadata.create_all(self.engine)
    
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
            "errors": [],
            "rows": []
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
            

