from fastapi import APIRouter, UploadFile, File  # Asegúrate de importar correctamente
from .service import GS1Service  # Ajusta la ruta según tu estructura

router = APIRouter()
gs1_service = GS1Service()

@router.post("/GS1-128/")
async def validate_codes(file: UploadFile = File(...)):
    contents = await file.read()  # Lee el contenido del archivo
    codes = contents.decode("utf-8").splitlines()  # Divide el contenido en líneas
    results = {code: gs1_service.validate_gs1_code(code) for code in codes}  # Valida cada código
    return results
