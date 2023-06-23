from core.models import *

TABLES = {
    "BOARD": Board,
    "THREAD": Thread,
    "REPLY": Reply,
    "POSTIDTRACKER": PostIdTracker
}

class ModelFactory:

    tables: dict

    def __init__(self, tables_config=None):
        if not tables_config:
            self.tables = TABLES
        else:
            self.tables = tables_config

    def get(self, model_id):

        model = None
        try:
            model = self.tables[model_id]
        except KeyError:
            print("Model not found for given key")

        return model

    def create_model_object(self, table_name):
        if table_name not in self.tables.keys():
            raise ValueError("Table name {} not recognized.".format(table_name))
        
        model_class = self.tables[table_name]
        model_object = model_class()
        
        return model_object