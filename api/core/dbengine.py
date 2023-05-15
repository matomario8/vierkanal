from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session

from .models import *

class DatabaseUtils:

    engine: Engine

    def __init__(self, dbhost: str):
        self.engine = create_engine(dbhost, echo=True)

    def init_tables(self, Model=Base):
        Model.metadata.create_all(self.engine)
    
    def add(self, item: Base) -> bool:
        """Adds the Base object to the db"""
        result = False
        msg = "Unable to get database session."
        with Session(self.engine) as session:
            try:
                session.add(item)
                session.commit()
                result = True
                msg = "Successfully added item into the database."
            except:
                msg = "Could not add the item to the database."
            
        return { "result": result, "msg": msg }

    def select(self, model, where=None):
        with Session(self.engine) as session:
            stmt = select(model)
            for item in session.scalars(stmt):
                print(item)
            

