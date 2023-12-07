# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475

### Products API ###

from fastapi import APIRouter

router = APIRouter(prefix="/organizaciones",
                   tags=["organizaciones"],
                   responses={404: {"message": "No encontrado"}})

organizaciones_list = ["Organizacion 1", "Organizacion 2",
                       "Organizacion 3", "Organizacion 4", "Organizacion 5"]


@router.get("/")
async def organizaciones():
    return organizaciones_list


# @router.get("/{id}")
# async def organizaciones_(id: int):
#     return organizaciones_list[id]
