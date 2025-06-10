from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class JobVacancy(BaseModel):
    position: str = Field(description="Job position title")
    company: str = Field(description="Company name")
    location: str = Field(description="Location of the job (city, country, region)")
    posted_date: str = Field(description="Date when the job was posted")
    url: str = Field(description="URL to the job posting")


class JobVacancyList(BaseModel):
    vacancies: List[JobVacancy] = Field(description="List of job vacancies found")
    is_available: bool = Field(
        description="Whether jobs were found and data is confident"
    )


class JobDetailResponse(BaseModel):
    position: str = Field(description="Job position title")
    company: str = Field(description="Company name")
    location: str = Field(description="Location of the job (city, country, region)")
    posted_date: str = Field(description="Date when the job was posted")
    responsibilities: List[str] = Field(description="List of job responsibilities")
    requirements: List[str] = Field(description="List of job requirements")
    salary: Optional[str] = Field(
        default=None, description="Salary information if available"
    )
    job_type: Optional[str] = Field(
        default=None, description="Job type (full-time, part-time, contract, etc.)"
    )
    description: Optional[str] = Field(
        default=None, description="Full job description text"
    )
    url: str = Field(description="URL to the job posting")
    benefits: Optional[List[str]] = Field(
        default=None, description="List of benefits and perks offered"
    )
    application_instructions: Optional[str] = Field(
        default=None, description="Instructions for applying to the job"
    )
    tech_stack: Optional[List[str]] = Field(
        default=None, description="List of technologies and tools used in the role"
    )
    work_model: Optional[str] = Field(
        default=None, description="Work model (On-site, Remote, Hybrid)"
    )
    contact_info: Optional[str] = Field(
        default=None, description="Contact details or support information"
    )
    seniority_level: Optional[str] = Field(
        default=None, description="Seniority level (Entry level, Mid-level, Senior, etc.)"
    )
    employment_type: Optional[str] = Field(
        default=None, description="Employment type (Full-time, Part-time, Contract, etc.)"
    )
    application_email: Optional[str] = Field(
        default=None, description="Email address for sending resumes"
    )
    what_youll_do: Optional[List[str]] = Field(
        default=None, description="List of key responsibilities and activities"
    )
    tools_and_platforms: Optional[List[str]] = Field(
        default=None, description="List of tools and platforms used (e.g., Git, Docker, Kubernetes, MLflow, Airflow, Jupyter)"
    )
    start_date: Optional[str] = Field(
        default=None, description="Expected start date or urgency of the position"
    )
    working_hours: Optional[str] = Field(
        default=None, description="Expected working hours and shift information"
    )
    number_of_openings: Optional[str] = Field(
        default=None, description="Number of positions available"
    )
    duration: Optional[str] = Field(
        default=None, description="Duration for contract roles"
    )
    collaboration_tools: Optional[List[str]] = Field(
        default=None, description="Tools used for collaboration (e.g., Slack, Jira, Notion)"
    )
    
    # New fields
    career_growth: Optional[List[str]] = Field(
        default=None, description="Career progression and development opportunities"
    )
    company_culture: Optional[List[str]] = Field(
        default=None, description="Company culture and work environment details"
    )
    application_process: Optional[str] = Field(
        default=None,
        description="Detailed application process including deadline, stages, and timeline"
    )
    additional_perks: Optional[List[str]] = Field(
        default=None, description="Additional perks and allowances"
    )
    work_life_balance: Optional[str] = Field(
        default=None,
        description="Work-life balance policies including leave, holidays, and flexibility"
    )
    project_details: Optional[str] = Field(
        default=None,
        description="Details about current projects, team size, and duration"
    )
    performance_metrics: Optional[str] = Field(
        default=None,
        description="Performance evaluation process and metrics"
    )
    onboarding_process: Optional[str] = Field(
        default=None,
        description="Onboarding and training process details"
    )
    technical_environment: Optional[str] = Field(
        default=None,
        description="Technical setup and infrastructure details"
    )
    company_info: Optional[str] = Field(
        default=None,
        description="Additional company information including size, industry, and achievements"
    )
    
    # Contact and Career Information
    career_mail: Optional[str] = Field(
        default=None, description="Career email address for applications"
    )
    hr_contact: Optional[str] = Field(
        default=None, description="HR contact information"
    )
    recruiter_contact: Optional[str] = Field(
        default=None, description="Recruiter contact information"
    )
    office_location: Optional[str] = Field(
        default=None, description="Office location details"
    )
    emergency_contact: Optional[str] = Field(
        default=None, description="Emergency contact information"
    )
