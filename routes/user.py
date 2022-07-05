from ctypes.wintypes import tagSIZE
from hashlib import new
from urllib import response
from fastapi import APIRouter, Response, status
from confing.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users', response_model=list[User], tags=["users"])
def find_all_user():
    return usersEntity(conn.test.user.find())

@user.post('/users', response_model=User, tags=["users"])
def create_user(user:User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.test.user.insert_one(new_user).inserted_id
    user = conn.test.user.find_one({"_id":id})
    return userEntity(user)



@user.get('/users/{id}', response_model=User, tags=["users"])
def find_user(id:str):
    return userEntity(conn.test.user.find_one({"_id":ObjectId(id)}))
    


@user.put('/users/{id}', response_model=User, tags=["users"])
def update_user(id:str, user:User):
    conn.test.user.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    return userEntity(conn.test.user.find_one({"_id":ObjectId(id)}))

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags =["users"])
def delete_user(id:str):
    userEntity(conn.test.user.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

