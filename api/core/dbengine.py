from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session

from .models import *

class DatabaseUtils:

    engine: Engine

    def __init__(self, dbhost: str):
        self.engine = create_engine(dbhost, echo=True)

    def init_tables(self, model=Base):
        model.metadata.create_all(self.engine)
    
    def add(self, model_object) -> bool:
        """Adds the Base object to the db"""
        result = False
        msg = "Unable to get database session."
        with Session(self.engine) as session:
            try:
                session.add(model_object)
                session.commit()
                result = True
                msg = "Successfully added item into the database."
            except:
                msg = "Could not add the item to the database."
            
        return { "result": result, "msg": msg }

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
            

