#   Importing fastapi
from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
import uvicorn
# creating instance of this fastapi
app = FastAPI()

# This app is actually very important, actually the name is very important 

# @app.get('/blog') # Path operation decorator
@app.get('/blog') # Path operation decorator
def index(limit=10, published:bool =  True, sort: Optional[str] = None):
    # return {'data': {'name': 'Test'}}
    if published:
        return {'data': f'{limit} published blogs from the list'}
    else:
        return {'data': f'{limit} all blogs from the list'}
# If we try to call all the blog it is super inefficeint, suppose you have 1000+ data it will take some time to load, we have to limit or suppose we want only published data, what we can do is provide query parameter @app.get('/blog?limit=10&published=true'), but we dont want to hardcode this things, we can refer query paramenters from documentation

@app.get('/about')
def about():
    return {'data': {'name': 'About'}}

# This thing should be above @app.get('/blog/{id}'), bacause below one has dynamic routing as parameter so if call it down it will not show or throw error
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unplubl data'}

@app.get('/blog/{id}')
def show(id: int): # id accepted by function from decorator, here we can define int, so that it should accept only interger, same we can do it for string also typing as str. These int, str under parameter is called Pydantic
    return {'data':id}

# model start
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]  # This will be optional, every time we don't want to send data
# model end


@app.post('/blog')
# def create_blog(request: Blog):
def create_blog(blog: Blog): # We can give any name in replacement of request
    # return {'data': f'Blog is created with title as {request.title}'}
    return {'data': f'Blog is created with title as {blog.title}'}


# If we want to change the port, to that:
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

# to run the program, we have to type python3 main.py on terminal, as uvicorn will still run on 8000 port