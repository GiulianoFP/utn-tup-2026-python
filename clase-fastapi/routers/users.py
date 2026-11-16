from typing import Optional
from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


# 1. GET con filtro opcional por is_active (Completa la Parte 1)
@router.get("/user")
def get_users(is_active: Optional[bool] = None) -> GetUsersResponse:
    if is_active is not None:
        filtered_users = [user for user in usuarios if user.is_active == is_active]
        return GetUsersResponse(users=filtered_users)
    return GetUsersResponse(users=usuarios)


# 2. POST para crear usuario (Ya lo tenías)
@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")


# 3. PUT para modificar un usuario existente (Completa la Parte 1)
@router.put("/user/{id}")
def update_user(id: int, updated_user: User) -> CreateUserResponse:
    for index, user in enumerate(usuarios):
        if user.id == id:
            # Mantenemos el ID de la URL y reemplazamos los datos
            updated_user.id = id
            usuarios[index] = updated_user
            return CreateUserResponse(message="Usuario actualizado correctamente")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


# 4. DELETE para borrar usuario (Ya lo tenías)
@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="usuario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )