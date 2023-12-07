### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.usuario import *
from db.schemas.usuario import *
from db.client import *

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Usuario])
async def usuarios():
    return usuarios_schema(db_client.users.find())


@router.get("/{id}")  # Path
async def usuario(id: str):
    return search_usuario("_id", ObjectId(id))


@router.get("/")  # Query
async def usuario(id: str):
    return search_usuario("_id", ObjectId(id))


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def usuario(usuario: Usuario):
    if type(search_usuario("email", usuario.email)) == Usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    usuario_dict = dict(usuario)
    del usuario_dict["id"]

    id = db_client.usuarios.insert_one(usuario_dict).inserted_id

    new_usuario = usuario_schema(db_client.usuarios.find_one({"_id": id}))

    return Usuario(**new_usuario)


@router.put("/", response_model=Usuario)
async def usuario(usuario: Usuario):

    usuario_dict = dict(usuario)
    del usuario_dict["id"]

    try:
        db_client.usuarios.find_one_and_replace(
            {"_id": ObjectId(usuario.id)}, usuario_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_usuario("_id", ObjectId(usuario.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def usuario(id: str):

    found = db_client.usuarios.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}

# Helper


def search_usuario(field: str, key):

    try:
        usuario = db_client.usuarios.find_one({field: key})
        return Usuario(**usuario_schema(usuario))
    except:
        return {"error": "No se ha encontrado el usuario"}
