from fastapi import FastAPI
from pydantic import BaseModel
from schemas import Blog
# or 
# from . import schemas
# from . import schemas, models
import models
import schemas
from database import engine
app = FastAPI()


# most important line as it creates db
models.Base.metadata.create_all(engine)


# Crud operation
# Create a blog
# @app.post('/blog')
# def create(title, body):
#     return {'title': title, 'body': body}

# We need pydentic model, rather using above thing:
# class Blog(BaseModel):
#     title: str
#     body: str

# above thing moved to schemas.py file

@app.post('/blog')
def create(request: Blog):
    return request

# We will get request body, rather then input field
