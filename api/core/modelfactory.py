from .models import *

class Tables:
    pass

TABLES = Tables()
TABLES.BOARD = "BOARD"
TABLES.THREAD = "THREAD"
TABLES.REPLY = "REPLY"
TABLES.POSTIDTRACKER = "POSTIDTRACKER"

TABLES_LIST = [TABLES.BOARD, TABLES.THREAD, TABLES.REPLY, TABLES.POSTIDTRACKER]

def create_model_object(table_name: Base):
    if table_name not in TABLES_LIST:
        raise ValueError("Table name {} not recognized.".format(table_name))
    
    model_object = None

    if table_name == TABLES.BOARD:
        model_object = Board()
    elif table_name == TABLES.THREAD:
        model_object = Thread()
    elif table_name == TABLES.REPLY:
        model_object = Reply()
    elif table_name == TABLES.POSTIDTRACKER:
        model_object = PostIdTracker()
    else:
        raise ValueError("Table name {} was recognized, but a handler \
                         doesn't exist for it.".format(table_name))
    
    return model_object