from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/") # @ -> decorator, get -> path operation
async def root():
    return {"message": "Hello World"}

# request Get method url: "/posts"
@app.get("/posts")
def get_posts():
    return {"data":"Your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    return {"data": "new_post"}    

# title str, content str
