from .service import GS1Service

gs1_service = GS1Service()

def validate_gs1_code(code: str):
    if gs1_service.validate(code):
        return {"message": "Código válido"}
    else:
        return {"message": "Código no válido"}
