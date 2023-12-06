### Modelo Usuario ###

from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    email: str
    password: str
