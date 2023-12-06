### schema de clase Organizacion  ###

def org_schema(organizacion) -> dict:
    return {"id": str(organizacion["_id"]),
            "nombre": organizacion["username"],
            "apellido": organizacion["surname"],
            "email": organizacion["email"],
            "password": organizacion["password"], }


def orgs_schema(organizaciones) -> list:
    return [org_schema(organizacion) for organizacion in organizaciones]
