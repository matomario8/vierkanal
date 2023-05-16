from .models import *

TABLES = {
    "BOARD": Board,
    "THREAD": Thread,
    "REPLY": Reply,
    "POSTIDTRACKER": PostIdTracker
}

class ModelFactory:

    tables: dict

    def __init__(self, *args, **kwargs):
        if "tables_config" not in kwargs:
            self.tables = TABLES
        else:
            self.tables = kwargs["tables_config"]

    def create_model_object(self, table_name):
        if table_name not in self.tables.keys():
            raise ValueError("Table name {} not recognized.".format(table_name))
        
        model_class = self.tables[table_name]
        model_object = model_class()
        
        return model_object