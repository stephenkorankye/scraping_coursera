from fastapi import FastAPI     
from os.path import isfile
from fastapi import Response
from mimetypes import guess_type


from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum  



app = FastAPI() 


class Category(BaseModel):
    category : str 
    
   
   



@app.get("/{filename}")
async def get_site(filename):
    filename = './' + filename

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename) as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)




@app.get("/")
async def home(): 
    print ( "Hello world" ) 
    return await get_site('index.html')


@app.post("/scrape")
async def scrape_it(data : Response):
    print (  ) 
    return { "q" : True } 