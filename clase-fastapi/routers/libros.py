from typing import Optional
from fastapi import APIRouter, HTTPException, status
from models.libros import (
    Libro,
    GetLibrosResponse,
    CreateLibroResponse,
    DeleteLibroResponse,
)

router = APIRouter()

# Base de datos temporal en memoria
libros: list[Libro] = [
    Libro(id=1, titulo="Cien anios de soledad", autor="Gabriel Garcia Marquez", paginas=417, disponible=True),
    Libro(id=2, titulo="Rayuela", autor="Julio Cortazar", paginas=600, disponible=False),
]


# 1. READ (Listar y filtrar por disponibilidad)
@router.get("/libro")
def get_libros(disponible: Optional[bool] = None) -> GetLibrosResponse:
    if disponible is not None:
        filtered_libros = [libro for libro in libros if libro.disponible == disponible]
        return GetLibrosResponse(libros=filtered_libros)
    return GetLibrosResponse(libros=libros)


# 2. CREATE (Crear un libro nuevo)
@router.post("/libro")
def create_libro(libro: Libro) -> CreateLibroResponse:
    libros.append(libro)
    return CreateLibroResponse(message="Libro creado exitosamente")


# 3. UPDATE (Modificar un libro existente por ID)
@router.put("/libro/{id}")
def update_libro(id: int, updated_libro: Libro) -> CreateLibroResponse:
    for index, libro in enumerate(libros):
        if libro.id == id:
            updated_libro.id = id  # Mantenemos el ID original de la URL
            libros[index] = updated_libro
            return CreateLibroResponse(message="Libro actualizado correctamente")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado"
    )


# 4. DELETE (Eliminar un libro por ID)
@router.delete("/libro/{id}")
def delete_libro(id: int) -> DeleteLibroResponse:
    for libro in libros:
        if libro.id == id:
            libros.remove(libro)
            return DeleteLibroResponse(message="Libro borrado exitosamente")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado"
    )