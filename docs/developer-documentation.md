# AI JobGenie - Developer Documentation v1.0

## Table of Contents
1. Project Overview
2. System Architecture
3. Technology Stack
4. Project Structure
5. Setup and Installation
6. API Documentation
7. Deployment Guide

## 1. Project Overview

AI JobGenie is an intelligent job search and application platform that leverages AI to help users find and apply for jobs more effectively. The application provides personalized job recommendations, automated application processes, and career insights.

### Key Features
- AI-powered job matching
- Automated job applications
- Resume parsing and optimization
- Career insights and analytics
- User profile management
- Job search and filtering

## 2. System Architecture

The application follows a modern microservices architecture with a clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                     Client Layer                        │
│  ┌─────────────┐     ┌─────────────┐     ┌──────────┐  │
│  │  Frontend   │     │   Backend   │     │  Storage │  │
│  │ (Streamlit) │◄───►│  (FastAPI)  │◄───►│  (Local) │  │
│  └─────────────┘     └─────────────┘     └──────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 3. Technology Stack

- **Frontend**: 
  - Streamlit
  - HTML/CSS
  - JavaScript

- **Backend**:
  - FastAPI
  - Python 3.11+
  - SQLAlchemy
  - Pydantic

- **Database**:
  - SQLite
  - SQLAlchemy ORM

- **AI/ML**:
  - OpenAI API
  - LangChain
  - Python NLP libraries

## 4. Project Structure

```
ai-jobgenie/
├── app/
│   ├── frontend/
│   │   └── streamlit_app.py
│   ├── api/
│   │   ├── routes/
│   │   └── models/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   └── main.py
├── database/
│   ├── models.py
│   └── operations.py
├── docs/
│   └── developer-documentation.md
├── tests/
├── uploads/
├── requirements.txt
├── start.sh
└── README.md
```

## 5. Setup and Installation

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/Pahinithi/ai_job_assistant.git
cd ai_job_assistant
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Starting the Application

You have two options to start the application:

#### Option 1: Using start script (Recommended)
```bash
# Make the script executable (first time only)
chmod +x start.sh

# Start both servers
./start.sh
```

#### Option 2: Manual start
```bash
# Terminal 1 - Start FastAPI server
fastapi dev app/main.py

# Terminal 2 - Start Streamlit app
streamlit run app/frontend/streamlit_app.py
```

### Accessing the Application
- Streamlit Frontend: http://localhost:8501
- FastAPI Backend: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 6. API Documentation

### FastAPI Endpoints

#### Authentication
- POST `/auth/login`
- POST `/auth/register`
- POST `/auth/logout`

#### User Profile
- GET `/users/me`
- PUT `/users/me`
- GET `/users/{user_id}`

#### Jobs
- GET `/jobs`
- GET `/jobs/{job_id}`
- POST `/jobs/apply`
- GET `/jobs/recommendations`

#### Applications
- GET `/applications`
- POST `/applications`
- GET `/applications/{application_id}`

## 7. Deployment Guide

### Local Development
1. Run `./start.sh` to start both FastAPI and Streamlit servers
2. Access Streamlit at `http://localhost:8501`
3. Access FastAPI at `http://localhost:8000`

### Production Deployment
1. Set up environment variables
2. Configure database
3. Deploy using Docker
4. Set up reverse proxy (Nginx/Apache)

## Contact

For any questions or support, please contact:
- Developer: Nithilan Pahirathan
- Email: nithilan32@gmail.com
- GitHub: https://github.com/Pahinithi

## Database Management

### Clearing and Reinitializing Database

To clear the existing database and start fresh:

```bash
# Remove existing database
rm database/sgpa.db

# Initialize new database
python database/init_db.py
```

Expected output:
```
Initializing database...
Database initialized successfully!
```

## Email Configuration

### Generate an App Password

After 2FA is enabled, follow these steps to generate an app password:

1. Go to: https://myaccount.google.com/apppasswords
2. Sign in again (for security)
3. Under "Select app", choose:
   - Mail
4. Under "Select device", choose:
   - Other (Custom name) → give it a name like EmailAgent
5. Click "Generate"
6. Google will generate a 16-character app password

### Environment Variables

Add the following to your `.env` file:

```bash
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-16-character-app-password
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
```

### Security Notes
- Never commit your app password to version control
- Keep your `.env` file secure and add it to `.gitignore`
- Regularly rotate your app passwords
- Use environment variables for all sensitive credentials 