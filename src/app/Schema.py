from pydantic import BaseModel

class Request(BaseModel):
    post_body:str
    id:str
    post_languages:str

class Response(BaseModel):
    result:str
    id:str
