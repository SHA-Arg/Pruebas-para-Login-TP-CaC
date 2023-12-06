### usuarios API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


# # Inicia el server: uvicorn usuarios:app --reload

router = APIRouter()


@router.get("/usuarios")
async def usuarios():
    return usuarios_list


@router.get("/usuario/{id}")  # Path
async def usuario(id: int):
    return search_usuario(id)


@router.get("/usuario/")  # Query
async def usuario(id: int):
    return search_usuario(id)


@router.post("/usuario/", response_model=usuario, status_code=201)
async def usuario(usuario: usuario):
    if type(search_usuario(usuario.id)) == usuario:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    usuarios_list.append(usuario)
    return usuario


@router.put("/usuario/")
async def usuario(usuario: usuario):
    found = False
    for index, saved_usuario in enumerate(usuarios_list):
        if saved_usuario.id == usuario.id:
            usuarios_list[index] = usuario
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return usuario


@router.delete("/usuario/{id}")
async def usuario(id: int):
    found = False
    for index, saved_usuario in enumerate(usuarios_list):
        if saved_usuario.id == id:
            del usuarios_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_usuario(id: int):
    usuarios = filter(lambda usuario: usuario.id == id, usuarios_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
