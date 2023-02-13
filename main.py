#   Importing fastapi
from fastapi import FastAPI

# creating instance of this fastapi
app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Test'}}

@app.get('/about')
def about():
    return {'data': {'name': 'About'}}
