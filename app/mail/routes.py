from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List, Optional
from .email_agent import EmailAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

# Initialize email agent with environment variables
email_agent = EmailAgent(
    smtp_server=os.getenv("SMTP_SERVER", "smtp.gmail.com"),
    smtp_port=int(os.getenv("SMTP_PORT", "587")),
    username=os.getenv("EMAIL_USERNAME"),
    password=os.getenv("EMAIL_PASSWORD")
)

@router.post("/upload-resume")
async def upload_resume(
    resume: UploadFile = File(...),
    candidate_name: str = Form(...),
    company_name: str = Form(...),
    position: str = Form(...),
    to_email: str = Form(...),
    cc_emails: Optional[str] = Form(None),
    custom_message: Optional[str] = Form(None)
):
    """
    Upload resume and send it to company email
    """
    try:
        # Read resume file
        resume_content = await resume.read()
        
        # Upload resume
        resume_path = email_agent.upload_resume(resume_content, resume.filename)
        
        # Generate email body
        body = email_agent.generate_email_body(
            company_name=company_name,
            position=position,
            candidate_name=candidate_name,
            custom_message=custom_message
        )
        
        # Prepare CC emails
        cc_list = cc_emails.split(",") if cc_emails else None
        
        # Send email
        success = email_agent.send_resume(
            to_email=to_email,
            subject=f"Application for {position} position at {company_name}",
            body=body,
            resume_path=resume_path,
            company_name=company_name,
            cc_emails=cc_list
        )
        
        if success:
            return {
                "status": "success",
                "message": f"Resume sent successfully to {company_name}"
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to send email"
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 