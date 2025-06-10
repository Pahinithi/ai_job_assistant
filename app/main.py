from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utlits.openai_functions import OpenAIFunctions
from app.utlits.openai_response_schemas import JobVacancyList, JobDetailResponse
from .routes import router as job_router
from .mail.routes import router as mail_router

app = FastAPI(title="AI Job Assistant API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(job_router, prefix="/api/v1")
app.include_router(mail_router, prefix="/api/v1/mail")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Job Assistant API"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/job-vacancies")
async def get_job_vacancies(position: str, place: str) -> JobVacancyList:
    oaif = OpenAIFunctions()
    vacancies = oaif.get_job_vacancies(position, place)
    return vacancies


@app.get("/job-details")
async def get_job_details(
    position: str, company: str, location: str
) -> JobDetailResponse:
    oaif = OpenAIFunctions()
    details = await oaif.get_job_details(position, company, location)
    return details
