from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 


from typing import Any 

app = FastAPI() 


@app.get("/")
async def home(): 
    print ( "Hello world" ) 
    return { "name" : "Hello world" } 
