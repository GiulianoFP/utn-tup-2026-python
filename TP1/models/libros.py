from pydantic import BaseModel
from typing import List


class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    paginas: int
    disponible: bool = True  

class GetLibrosResponse(BaseModel):
    libros: List[Libro]


class CreateLibroResponse(BaseModel):
    message: str


class DeleteLibroResponse(BaseModel):
    message: str