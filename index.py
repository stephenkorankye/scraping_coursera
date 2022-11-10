from fastapi import FastAPI , Form   
from os.path import isfile
from fastapi import Response , Request
# from starlette.responses import Response
from mimetypes import guess_type

from pydantic import BaseModel, Field

from scraper import get_scraper



app = FastAPI() 


class Category(BaseModel):
    name : str 
      



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
async def scrape_it( data : Request):
    nn = await data.body()
    nn = str(nn) 
    nn = nn.split('b')[1] 
    nn = nn.strip("''") 
    print ( nn ) 
    ans , value = get_scraper(nn) 
   
    if ans : 
        return { "success" : True } 
   
    return { "success" : True } 