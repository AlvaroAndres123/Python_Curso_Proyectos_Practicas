from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url : str
    age: int

users_list = [User(id=1, name="Alvaro",surname="Casco",url="https//almasoft.com", age=17),
        User(name="Jesua",surname="Lopez",url="https//turtle.com",age=22),
        User(name="Andres",surname="Guido",url="https//montype",age= 35)]
    

@app.get("/usersjson")
async def users():
    return [{"name": "Alvaro", "surname":"Casco","url":"https//almasoft.com","age":17},
            {"name": "Jesua", "surname":"Lopez","url":"https//turtle.com","age":22},
            {"name": "Andres", "surname":"Guido","url":"https//montype.com","age": 46}]


@app.get("/users")
async def userclass():
    return users_list

@app.get("/users/{id}")
async def user(id: int):
    users = filter(lambda usSer: user.id == 5, users_list)
    return list(users)