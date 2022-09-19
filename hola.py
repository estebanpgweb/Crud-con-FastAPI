from datetime import datetime
from logging import root
from turtle import title
from typing import Text, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uid
parcial = FastAPI()
posts= []  
class Post(BaseModel):
    id:Optional[str]
    titulo: str 
    autor: str
    contenido: Text
    fecha: datetime = datetime.now()
    publicacion: Optional[datetime]
    publicado: bool = False




#@parcial.get('/')
#def read_root():
 #   return {"Bienvenido2":"Bienvenido a mi API"}
@parcial.get('/posts')
def get_posts():
    return posts
@parcial.post('/posts')
def guardar_posts(post:Post):
    post.id= str(uid())
    posts.append(post.dict())
    return posts[-1]

#consulta para obtener un unico dato por id
@parcial.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
                 return post
    raise HTTPException (status_code= 404, detail="no encontrado")

#eliminacion por id
@parcial.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"ha sido eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="no encontrado")

#actualizar
@parcial.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["titulo"]= updatedPost.dict()["titulo"]
            posts[index]["contenido"]= updatedPost.dict()["contenido"]
            posts[index]["autor"]= updatedPost.dict()["autor"]
            return {"ha sido modificado exitosamente"}
    raise HTTPException(status_code=404, detail="no ha sido encontrado")