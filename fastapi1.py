
#pip install fastapi
#pip install fastapi[all]
#pip install "uvicorn[standard]"
#uvicorn fastapi1:app
#uvicorn fastapi1:app --reload  don't use it
from fastapi import FastAPI,Path

app=FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"moussa"}}
    
@app.get('/home')    
def jij():
    return "jihadov"