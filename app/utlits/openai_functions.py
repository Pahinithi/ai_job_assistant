from crawl4ai import AsyncWebCrawler
from openai import OpenAI
from app.settings import settings
from app.utlits.openai_response_schemas import JobVacancyList, JobDetailResponse


class OpenAIFunctions:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_job_vacancies(self, position: str, place: str) -> JobVacancyList:
        """
        Use OpenAI to find/collect recent job vacancies for a given position and place.
        """
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-search-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a job search assistant. Find recent job vacancies for the given position and place. Return a structured list of jobs with position, company, location, posted_date, and url.",
                },
                {
                    "role": "user",
                    "content": f"position: {position}\nplace: {place}",
                },
            ],
            response_format=JobVacancyList,
        )
        return response.choices[0].message.parsed

    async def get_job_details(self, position: str, company: str, location: str) -> JobDetailResponse:
        """
        Use OpenAI and Crawl4AI to extract job details for a given position, company, and location.
        """
        # First, use OpenAI to find the most relevant job posting URL
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-search-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a job search assistant. Find the most relevant job posting URL for the given position, company, and location.",
                },
                {
                    "role": "user",
                    "content": f"position: {position}\ncompany: {company}\nlocation: {location}",
                },
            ],
            response_format=JobVacancyList,
        )
        job_list = response.choices[0].message.parsed
        if not job_list.vacancies:
            raise Exception("No job posting found for the given position and company.")
        job_url = job_list.vacancies[0].url

        # Scrape the job posting page using Crawl4AI
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=job_url)
            scraped_content = result.markdown

        # Use OpenAI to extract job details from the scraped content
        details_response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role": "system",
                    "content": """Extract all job details from the following job posting page. Return a comprehensive set of information including:
                    - Position title
                    - Company name
                    - Location
                    - Job type and employment type
                    - Posted date
                    - Detailed description
                    - Responsibilities and what you'll do
                    - Requirements and qualifications
                    - Salary and compensation
                    - Benefits and perks
                    - Application instructions
                    - Tech stack and tools used
                    - Work model (On-site, Remote, Hybrid)
                    - Contact details and support info
                    - Seniority level
                    - Application email for resumes
                    - Tools and platforms used (Git, Docker, Kubernetes, MLflow, Airflow, Jupyter, etc.)
                    - Expected start date or urgency
                    - Working hours and shift information
                    - Number of positions available
                    - Duration for contract roles
                    - Collaboration tools used (Slack, Jira, Notion, etc.)
                    - Career growth and development opportunities
                    - Company culture and work environment
                    - Detailed application process (deadline, stages, timeline)
                    - Additional perks and allowances
                    - Work-life balance policies
                    - Project details (current projects, team size, duration)
                    - Performance metrics and evaluation process
                    - Onboarding process and training
                    - Technical environment setup
                    - Company information (size, industry, achievements)
                    - Career email address
                    - HR contact information
                    - Recruiter contact information
                    - Office location details
                    - Emergency contact information
                    Make sure to extract as much information as possible from the job posting. Format all information as strings or lists of strings.""",
                },
                {
                    "role": "user",
                    "content": f"Job posting page content:\n{scraped_content}\nURL: {job_url}",
                },
            ],
            response_format=JobDetailResponse,
        )
        return details_response.choices[0].message.parsed
