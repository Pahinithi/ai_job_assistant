import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List, Dict, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailAgent:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the email agent with SMTP server details
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            username: Email username
            password: Email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.upload_dir = Path("uploads/resumes")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def upload_resume(self, resume_file: bytes, filename: str) -> str:
        """
        Upload and save resume file
        
        Args:
            resume_file: Resume file content in bytes
            filename: Original filename
            
        Returns:
            str: Path to saved resume file
        """
        try:
            # Create uploads directory if it doesn't exist
            self.upload_dir.mkdir(parents=True, exist_ok=True)
            
            # Save file
            file_path = self.upload_dir / filename
            with open(file_path, "wb") as f:
                f.write(resume_file)
            
            logger.info(f"Resume uploaded successfully: {file_path}")
            return str(file_path)
        except Exception as e:
            logger.error(f"Error uploading resume: {str(e)}")
            raise

    def send_resume(self, 
                   to_email: str,
                   subject: str,
                   body: str,
                   resume_path: str,
                   company_name: str,
                   cc_emails: Optional[List[str]] = None) -> bool:
        """
        Send resume to company email
        
        Args:
            to_email: Recipient email address
            subject: Email subject
            body: Email body text
            resume_path: Path to resume file
            company_name: Name of the company
            cc_emails: List of CC email addresses
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            if cc_emails:
                msg['Cc'] = ', '.join(cc_emails)
            
            # Add body
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach resume
            with open(resume_path, 'rb') as f:
                resume = MIMEApplication(f.read(), _subtype='pdf')
                resume.add_header('Content-Disposition', 'attachment', filename=os.path.basename(resume_path))
                msg.attach(resume)
            
            # Connect to SMTP server and send
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                
                # Get all recipients
                recipients = [to_email]
                if cc_emails:
                    recipients.extend(cc_emails)
                
                # Send email
                server.send_message(msg, self.username, recipients)
            
            logger.info(f"Resume sent successfully to {company_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending resume to {company_name}: {str(e)}")
            return False

    def generate_email_body(self, 
                          company_name: str,
                          position: str,
                          candidate_name: str,
                          custom_message: Optional[str] = None) -> str:
        """
        Generate email body text
        
        Args:
            company_name: Name of the company
            position: Position being applied for
            candidate_name: Name of the candidate
            custom_message: Optional custom message to include
            
        Returns:
            str: Generated email body text
        """
        body = f"""Dear {company_name} Hiring Team,

I hope this email finds you well. I am writing to express my interest in the {position} position at {company_name}.

{custom_message if custom_message else f'I am excited about the opportunity to contribute to {company_name} and believe my skills and experience align well with the requirements for this role.'}

I have attached my resume for your review. I would welcome the opportunity to discuss how my background and skills could benefit {company_name}.

Thank you for considering my application.

Best regards,
{candidate_name}
"""
        return body 