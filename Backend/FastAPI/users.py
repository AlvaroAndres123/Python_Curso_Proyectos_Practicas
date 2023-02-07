from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list =[User(name= "Alvaro",surname= "Casco",url= "https://almasoft.com.ni",age= 17),
             User(name= "Jesua",surname= "Lopez",url= "https://gutierrezcia.com.ni",age= 22),
             User(name="Francisco",surname= "Guido",url= "https://sinriesgo.com.ni",age= 42),]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Alvaro", "surname":"Casco","url":"https://almasoft.com.ni","age":16},
            {"name":"Jesua", "surname":"Lopez","url":"https://gutierrezcia.com.ni","age":22},
            {"name":"Francisco", "surname":"Guido","url":"https://sinriesgo.com.ni","age":42}]

@app.get("/users")
async def users():
    return users_list