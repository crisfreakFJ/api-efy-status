from fastapi import APIRouter, HTTPException
from fastapi import status

from services.resultados_correo_service import ResultsService

service = ResultsService()

router = APIRouter(prefix="/api/v1")

@router.get("/resultados-correos/{id}", status_code=status.HTTP_200_OK)
async def get_results(id):
    response = service.get_results_from_survey(id)
    if not response:
        raise HTTPException(status_code=422, detail="Something was wrong with the service")
    return {"count":response}