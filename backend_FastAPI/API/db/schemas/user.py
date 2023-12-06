### schema de claseUsuario ###

def usuario_schema(usuario) -> dict:
    return {"id": str(usuario["_id"]),
            "nombre": usuario["username"],
            "apellido": usuario["surname"],
            "email": usuario["email"],
            "password": usuario["password"], }


def usuarios_schema(usuarios) -> list:
    return [usuario_schema(usuario) for usuario in usuarios]
