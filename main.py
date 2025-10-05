from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'DevBasscee'}}

@app.get('/')
def about():
    return {'data':{'name':'about page'}}