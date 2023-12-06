### Modelo de Organizacion ###

from pydantic import BaseModel
from typing import Optional


class Organizacion(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    direccion: str
    email: str
    password: str
