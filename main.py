from fastapi import FastAPI

import models
from router import blog, user, authentication
from database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.get('/')
def home():
    return 'Hello World..!!'



