import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import streamlit as st
import requests
import json
from typing import Dict, Any, List
import pandas as pd
from io import BytesIO

# Configure the page
st.set_page_config(
    page_title="AIJobGenie",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI with better arrangement
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    /* Header styling */
    .header {
        background: linear-gradient(120deg, var(--header-gradient-start), var(--header-gradient-end));
        color: var(--header-text);
        padding: 3.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        z-index: 1;
    }
    
    .header h1 {
        font-size: 2.8rem;
        margin-bottom: 1.2rem;
        font-weight: 700;
        position: relative;
        z-index: 2;
    }
    
    .header p {
        font-size: 1.3rem;
        opacity: 0.9;
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }
    
    /* Form styling */
    .stForm {
        background-color: var(--card-background);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        font-size: 1.1rem;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        border: 2px solid var(--border-color);
        background-color: var(--input-background);
        color: var(--text-color);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 4px var(--focus-shadow);
        transform: translateY(-1px);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(120deg, var(--button-gradient-start), var(--button-gradient-end));
        color: var(--button-text);
        padding: 1rem 2.5rem;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
        display: block;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
    }
    
    /* Job details card styling */
    .job-detail-card {
        background-color: var(--card-background);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .job-detail-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(to bottom, var(--button-gradient-start), var(--button-gradient-end));
    }
    
    .job-detail-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }
    
    .detail-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .detail-item {
        background-color: var(--item-background);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 4px solid var(--primary-color);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .detail-item::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .detail-item:hover {
        background-color: var(--item-hover);
        transform: translateX(4px);
    }
    
    .detail-item:hover::after {
        opacity: 1;
    }
    
    .detail-label {
        font-size: 0.9rem;
        color: var(--label-color);
        margin-bottom: 0.6rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
    }
    
    .detail-value {
        font-size: 1.2rem;
        color: var(--text-color);
        font-weight: 500;
        line-height: 1.6;
    }
    
    .tag {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: linear-gradient(120deg, var(--tag-gradient-start), var(--tag-gradient-end));
        color: var(--tag-text);
        border-radius: 25px;
        margin: 0.3rem;
        font-size: 0.95rem;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .section-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid var(--border-color);
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100px;
        height: 2px;
        background: linear-gradient(to right, var(--button-gradient-start), var(--button-gradient-end));
    }
    
    .section-header h3 {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--header-text);
        margin: 0;
    }
    
    .contact-button {
        display: inline-block;
        padding: 1rem 2rem;
        background: linear-gradient(120deg, var(--button-gradient-start), var(--button-gradient-end));
        color: var(--button-text);
        text-decoration: none;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 100%;
        max-width: 300px;
        margin: 1.5rem auto;
    }
    
    .contact-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: var(--card-background);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 4rem;
        white-space: pre-wrap;
        background-color: var(--tab-background);
        border-radius: 12px;
        gap: 1rem;
        padding: 1rem;
        transition: all 0.3s ease;
        color: var(--text-color);
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(120deg, var(--button-gradient-start), var(--button-gradient-end));
        color: var(--button-text);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2.5rem;
        color: var(--text-color);
        font-size: 1rem;
        opacity: 0.8;
        margin-top: 3rem;
        border-top: 1px solid var(--border-color);
    }

    /* CSS Variables for theme support */
    :root {
        /* Light theme (default) */
        --background-color: #e9ecef;
        --card-background: #f8f9fa;
        --text-color: #222831;
        --header-text: #006064;
        --label-color: #546e7a;
        --border-color: #d1d5db;
        --input-background: #ffffff;
        --item-background: #f1f3f4;
        --item-hover: #e0e0e0;
        --tab-background: #f1f3f4;
        --primary-color: #80deea;
        --header-gradient-start: #e0f7fa;
        --header-gradient-end: #b2ebf2;
        --button-gradient-start: #80deea;
        --button-gradient-end: #4dd0e1;
        --button-text: #006064;
        --tag-gradient-start: #e0f7fa;
        --tag-gradient-end: #b2ebf2;
        --tag-text: #006064;
        --focus-shadow: rgba(128, 222, 234, 0.2);
    }

    /* Dark theme */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #1a1a1a;
            --card-background: #2d2d2d;
            --text-color: #ffffff;
            --header-text: #ffffff;
            --label-color: #b0bec5;
            --border-color: #404040;
            --input-background: #2d2d2d;
            --item-background: #363636;
            --item-hover: #404040;
            --tab-background: #363636;
            --primary-color: #80deea;
            --header-gradient-start: #006064;
            --header-gradient-end: #00838f;
            --button-gradient-start: #00838f;
            --button-gradient-end: #006064;
            --button-text: #ffffff;
            --tag-gradient-start: #00838f;
            --tag-gradient-end: #006064;
            --tag-text: #ffffff;
            --focus-shadow: rgba(0, 150, 136, 0.3);
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Import login and signup page logic
login_path = Path(__file__).parent.parent / 'page' / 'login.py'
signup_path = Path(__file__).parent.parent / 'page' / 'signup.py'

def run_login():
    with open(login_path) as f:
        code = f.read()
    exec(code, globals())

def run_signup():
    with open(signup_path) as f:
        code = f.read()
    exec(code, globals())

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'show_signup' not in st.session_state:
    st.session_state['show_signup'] = False

if not st.session_state['logged_in']:
    # Only show login/signup, hide header and tabs
    st.markdown("""
        <style>
        .header, .stTabs {display: none !important;}
        </style>
    """, unsafe_allow_html=True)
    if st.session_state['show_signup']:
        run_signup()
        if st.button('Back to Login'):
            st.session_state['show_signup'] = False
    else:
        run_login()
        if st.button('Go to Sign Up'):
            st.session_state['show_signup'] = True
else:
    # Show header and main app tabs only after login
    st.markdown("""
        <div class="header">
            <h1>💼 AIJobGenie</h1>
            <p>Find your dream job with intelligent AI insights and effortless applications.</p>
        </div>
    """, unsafe_allow_html=True)
    main_tabs = st.tabs(["🔍 Search Job Vacancies", "📋 Job Details", "✉️ Email Agent"])

    # Function to display job vacancies
    def display_job_vacancies(vacancies: List[Dict[str, Any]]):
        if not vacancies:
            st.warning("No job vacancies found.")
            return
        
        for vacancy in vacancies:
            st.markdown(f"""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3>{vacancy['position']}</h3>
                    </div>
                    <div class="detail-grid">
                        <div class="detail-item">
                            <div class="detail-label">Company</div>
                            <div class="detail-value">{vacancy['company']}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Location</div>
                            <div class="detail-value">{vacancy['location']}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Posted Date</div>
                            <div class="detail-value">{vacancy['posted_date']}</div>
                        </div>
                    </div>
                    <div style="text-align: center; margin-top: 1rem;">
                        <a href="{vacancy['url']}" target="_blank" class="contact-button">View Job</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Function to display job details
    def display_job_details(details: Dict[str, Any]):
        # Add custom CSS for job details cards
        st.markdown("""
            <style>
            .job-detail-card {
                background-color: var(--card-background);
                border-radius: 15px;
                padding: 1.5rem;
                margin: 1rem 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease;
            }
            
            .job-detail-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }
            
            .detail-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1rem;
                margin: 1rem 0;
            }
            
            .detail-item {
                background-color: var(--card-background);
                padding: 1rem;
                border-radius: 10px;
                border-left: 4px solid var(--primary-color);
            }
            
            .detail-label {
                font-size: 0.9rem;
                color: var(--text-color);
                opacity: 0.8;
                margin-bottom: 0.3rem;
            }
            
            .detail-value {
                font-size: 1.1rem;
                color: var(--text-color);
                font-weight: 500;
            }
            
            .tag {
                display: inline-block;
                padding: 0.3rem 0.8rem;
                background-color: var(--primary-color);
                color: white;
                border-radius: 20px;
                margin: 0.2rem;
                font-size: 0.9rem;
            }
            
            .section-header {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin-bottom: 1rem;
                color: var(--primary-color);
            }
            
            .section-header i {
                font-size: 1.5rem;
            }
            
            .contact-button {
                display: inline-block;
                padding: 0.8rem 1.5rem;
                background-color: var(--primary-color);
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: all 0.3s ease;
                margin: 0.5rem 0;
            }
            
            .contact-button:hover {
                background-color: var(--primary-hover);
                transform: translateY(-2px);
            }
            </style>
        """, unsafe_allow_html=True)

        # Basic Information Card
        st.markdown(f"""
            <div class="job-detail-card">
                <div class="section-header">
                    <h2 style="margin: 0;">{details['position']}</h2>
                </div>
                <div class="detail-grid">
                    <div class="detail-item">
                        <div class="detail-label">Company</div>
                        <div class="detail-value">{details['company']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Location</div>
                        <div class="detail-value">{details['location']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Posted Date</div>
                        <div class="detail-value">{details['posted_date']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Job Type</div>
                        <div class="detail-value">{details['job_type'] or 'Not specified'}</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Company Information Card
        if details['company_info']:
            st.markdown(f"""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3 style="margin: 0;">About the Company</h3>
                    </div>
                    <p>{details['company_info']}</p>
                </div>
            """, unsafe_allow_html=True)

        # Description Card
        if details['description']:
            st.markdown(f"""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3 style="margin: 0;">Job Description</h3>
                    </div>
                    <p>{details['description']}</p>
                </div>
            """, unsafe_allow_html=True)

        # What You'll Do Card
        if details['what_youll_do']:
            st.markdown("""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3 style="margin: 0;">What You'll Do</h3>
                    </div>
                    <div style="display: grid; gap: 0.5rem;">
            """, unsafe_allow_html=True)
            for item in details['what_youll_do']:
                st.markdown(f"""
                    <div class="detail-item">
                        <div class="detail-value">{item}</div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

        # Requirements Card
        if details['requirements']:
            st.markdown("""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3 style="margin: 0;">Requirements</h3>
                    </div>
                    <div style="display: grid; gap: 0.5rem;">
            """, unsafe_allow_html=True)
            for req in details['requirements']:
                st.markdown(f"""
                    <div class="detail-item">
                        <div class="detail-value">{req}</div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

        # Technical Requirements Card
        if details['tech_stack'] or details['tools_and_platforms']:
            st.markdown("""
                <div class="job-detail-card">
                    <div class="section-header">
                        <h3 style="margin: 0;">Technical Requirements</h3>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            """, unsafe_allow_html=True)
            
            if details['tech_stack']:
                st.markdown("""
                    <div>
                        <h4 style="margin-bottom: 1rem;">Tech Stack</h4>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                """, unsafe_allow_html=True)
                for tech in details['tech_stack']:
                    st.markdown(f'<span class="tag">{tech}</span>', unsafe_allow_html=True)
                st.markdown("</div></div>", unsafe_allow_html=True)
            
            if details['tools_and_platforms']:
                st.markdown("""
                    <div>
                        <h4 style="margin-bottom: 1rem;">Tools & Platforms</h4>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                """, unsafe_allow_html=True)
                for tool in details['tools_and_platforms']:
                    st.markdown(f'<span class="tag">{tool}</span>', unsafe_allow_html=True)
                st.markdown("</div></div>", unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)

        # Contact Information Card
        st.markdown("""
            <div class="job-detail-card">
                <div class="section-header">
                    <h3 style="margin: 0;">Contact Information</h3>
                </div>
                <div class="detail-grid">
        """, unsafe_allow_html=True)
        
        contact_items = [
            ('Career Email', details['career_mail']),
            ('Application Email', details['application_email']),
            ('HR Contact', details['hr_contact']),
            ('Recruiter Contact', details['recruiter_contact']),
            ('Office Location', details['office_location']),
            ('Emergency Contact', details['emergency_contact'])
        ]
        
        for label, value in contact_items:
            if value:
                st.markdown(f"""
                    <div class="detail-item">
                        <div class="detail-label">{label}</div>
                        <div class="detail-value">{value}</div>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

        # Application Information Card
        st.markdown("""
            <div class="job-detail-card">
                <div class="section-header">
                    <h3 style="margin: 0;">Application Information</h3>
                </div>
                <div class="detail-grid">
        """, unsafe_allow_html=True)
        
        application_items = [
            ('How to Apply', details['application_instructions']),
            ('Application Process', details['application_process']),
            ('Start Date', details['start_date']),
            ('Working Hours', details['working_hours']),
            ('General Contact', details['contact_info'])
        ]
        
        for label, value in application_items:
            if value:
                st.markdown(f"""
                    <div class="detail-item">
                        <div class="detail-label">{label}</div>
                        <div class="detail-value">{value}</div>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

        # Original Job Posting Link
        st.markdown(f"""
            <div class="job-detail-card" style="text-align: center;">
                <a href="{details['url']}" target="_blank" class="contact-button">
                    View Original Job Posting
                </a>
            </div>
        """, unsafe_allow_html=True)

    # Job Vacancies Tab
    with main_tabs[0]:
        # Job Vacancies Tab Content
        with st.form("job_vacancies_form"):
            col1, col2 = st.columns(2)
            with col1:
                position = st.text_input("Position Title", placeholder="e.g., Software Engineer")
            with col2:
                place = st.text_input("Location", placeholder="e.g., New York")
            submit_vacancies = st.form_submit_button("🔍 Search Vacancies")
        if submit_vacancies:
            if position and place:
                try:
                    with st.spinner("Searching for job vacancies..."):
                        response = requests.get(
                            "http://localhost:8000/job-vacancies",
                            params={"position": position, "place": place}
                        )
                    if response.status_code == 200:
                        data = response.json()
                        if data['is_available']:
                            display_job_vacancies(data['vacancies'])
                        else:
                            st.warning("No job vacancies found.")
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please fill in all fields")

    # Job Details Tab
    with main_tabs[1]:
        # Job Details Tab Content
        with st.form("job_details_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                position = st.text_input("Position Title", placeholder="e.g., Software Engineer")
            with col2:
                company = st.text_input("Company Name", placeholder="e.g., Google")
            with col3:
                location = st.text_input("Location", placeholder="e.g., New York")
            submit_details = st.form_submit_button("📋 Get Job Details")
        if submit_details:
            if position and company and location:
                try:
                    with st.spinner("Fetching job details..."):
                        response = requests.get(
                            "http://localhost:8000/job-details",
                            params={"position": position, "company": company, "location": location}
                        )
                    if response.status_code == 200:
                        job_details = response.json()
                        display_job_details(job_details)
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please fill in all fields")

    # Email Agent Tab
    with main_tabs[2]:
        # Email Agent Tab Content
        st.markdown("""
            <div class="header">
                <h1>Email Agent</h1>
                <p>Upload your resume and send it to companies</p>
            </div>
        """, unsafe_allow_html=True)
        with st.form("resume_upload_form"):
            st.markdown("### Upload Resume")
            resume_file = st.file_uploader("Upload your resume (PDF)", type=['pdf'])
            col1, col2 = st.columns(2)
            with col1:
                candidate_name = st.text_input("Your Name")
                company_name = st.text_input("Company Name")
                position = st.text_input("Position")
            with col2:
                to_email = st.text_input("Company Email")
                cc_emails = st.text_input("CC Emails (comma-separated)")
                custom_message = st.text_area("Custom Message (optional)")
            submit_button = st.form_submit_button("Send Resume")
            if submit_button and resume_file:
                try:
                    files = {'resume': ('resume.pdf', resume_file.getvalue(), 'application/pdf')}
                    data = {
                        'candidate_name': candidate_name,
                        'company_name': company_name,
                        'position': position,
                        'to_email': to_email,
                        'cc_emails': cc_emails if cc_emails else None,
                        'custom_message': custom_message if custom_message else None
                    }
                    response = requests.post(
                        "http://localhost:8000/api/v1/mail/upload-resume",
                        files=files,
                        data=data
                    )
                    if response.status_code == 200:
                        st.success("Resume sent successfully!")
                    else:
                        st.error(f"Error: {response.json()['detail']}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            elif submit_button and not resume_file:
                st.error("Please upload a resume file")

# Footer
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by Nithilan</p>
    </div>
""", unsafe_allow_html=True)
