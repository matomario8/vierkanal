from __init__ import create_app

app = create_app("config.yml")
import api

#print(app.view_functions)