from fastapi import APIRouter
from app.utlits.openai_functions import OpenAIFunctions
from app.utlits.openai_response_schemas import JobVacancyList, JobDetailResponse

router = APIRouter()

@router.get("/job-vacancies")
async def get_job_vacancies(position: str, place: str) -> JobVacancyList:
    oaif = OpenAIFunctions()
    vacancies = oaif.get_job_vacancies(position, place)
    return vacancies

@router.get("/job-details")
async def get_job_details(
    position: str, company: str, location: str
) -> JobDetailResponse:
    oaif = OpenAIFunctions()
    details = await oaif.get_job_details(position, company, location)
    return details 