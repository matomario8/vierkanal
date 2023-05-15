from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import Session

from .models import *

class DBConnection:

    engine: Engine

    def __init__(self, dbhost: str):
        self.engine = create_engine(dbhost, echo=True)

    def init_tables(self):
        Base.metadata.create_all(self.engine)
    
    def insert(self, item: Base) -> bool:
        """Inserts the Base object to the db"""
        result = False
        msg = "Unable to get database session."
        with Session(self.engine) as session:
            try:
                session.add(item)
                session.commit()
                result = True
                msg = "Successfully inserted item into the database."
            except:
                msg = "Could not insert the item to the database."
            
        return { "result": result, "msg": msg }

    def select(self, model, where=None):
        with Session(self.engine) as session:
            stmt = select(model)
            for item in session.scalars(stmt):
                print(item)
            

