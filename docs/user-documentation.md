# AI JobGenie - User Documentation v1.0

## Table of Contents
1. Introduction
2. Getting Started
3. Features
4. User Guide
5. Troubleshooting
6. FAQ
7. Docker Setup Guide

## 1. Introduction

Welcome to AI JobGenie, your intelligent job search and application assistant. This platform helps you find and apply for jobs more effectively using AI-powered features.

### What is AI JobGenie?
AI JobGenie is a smart job search platform that:
- Matches you with relevant job opportunities
- Helps optimize your resume
- Provides career insights
- Streamlines the job application process

## 2. Getting Started

### System Requirements
- Modern web browser (Chrome, Firefox, Safari, or Edge)
- Internet connection
- Valid email address

### Creating an Account
1. Visit the application homepage
2. Click "Sign Up" or "Register"
3. Fill in your details:
   - Full Name
   - Email Address
   - Password
4. Verify your email address
5. Complete your profile

### Logging In
1. Go to the login page
2. Enter your email and password
3. Click "Login"

## 3. Features

### Job Search
- Search jobs by:
  - Keywords
  - Location
  - Job type
  - Experience level
  - Salary range
- Save favorite jobs
- Set up job alerts

### Resume Management
- Upload your resume
- Get AI-powered optimization suggestions
- Create multiple resume versions
- Track resume performance

### Application Tracking
- Track application status
- View application history
- Get application insights
- Set reminders for follow-ups

### Career Insights
- View job market trends
- Get salary insights
- Receive career recommendations
- Track application success rate

## 4. User Guide

### Dashboard
The dashboard is your central hub for:
- Recent job matches
- Application status
- Career insights
- Quick actions

### Job Search
1. Use the search bar to find jobs
2. Apply filters to narrow results
3. Click on job listings to view details
4. Save interesting jobs
5. Apply directly through the platform

### Resume Builder
1. Upload your existing resume
2. Get AI suggestions for improvements
3. Edit and customize your resume
4. Save different versions
5. Download in various formats

### Application Process
1. Select a job to apply for
2. Choose your resume version
3. Fill in required information
4. Review your application
5. Submit and track status

## 5. Troubleshooting

### Common Issues

#### Login Problems
- Check your internet connection
- Verify your email and password
- Use the "Forgot Password" feature
- Clear browser cache and cookies

#### Application Issues
- Ensure all required fields are filled
- Check file size limits for uploads
- Verify your resume format
- Try using a different browser

#### Technical Issues
- Refresh the page
- Clear browser cache
- Try incognito/private mode
- Update your browser

## 6. FAQ

### General Questions

#### How does AI JobGenie work?
AI JobGenie uses artificial intelligence to match your skills and preferences with job opportunities, optimize your resume, and provide career insights.

#### Is my data secure?
Yes, we use industry-standard security measures to protect your personal information and data.

#### Is the service free?
Basic features are free. Premium features are available with a subscription.

### Account Management

#### How do I reset my password?
1. Click "Forgot Password"
2. Enter your email
3. Follow the reset link
4. Create a new password

#### Can I delete my account?
Yes, you can delete your account in the settings menu. Note that this action is permanent.

### Job Search

#### How often are jobs updated?
Job listings are updated in real-time from various sources.

#### Can I apply to jobs outside the platform?
Yes, you can track applications made outside the platform by adding them manually.

## 7. Docker Setup Guide

### Quick Start with Docker

1. **Install Docker**
   - Download and install Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
   - Ensure Docker is running on your system

2. **Run the Application**
   ```bash
   # Start the application
   docker-compose up
   ```

3. **Access the Application**
   - Open your web browser
   - Go to http://localhost:8501
   - The application will be ready to use

### Stopping the Application
```bash
# Stop the application
docker-compose down
```

### Common Docker Commands

1. **View Application Status**
   ```bash
   # Check if containers are running
   docker-compose ps
   ```

2. **View Logs**
   ```bash
   # View application logs
   docker-compose logs
   ```

### Troubleshooting Docker

1. **Application Not Starting**
   - Ensure Docker is running
   - Check if ports 8000 and 8501 are available
   - Verify your environment variables

2. **Cannot Access Application**
   - Check if containers are running
   - Verify you're using the correct URL
   - Check application logs for errors

3. **Container Issues**
   - Restart the containers:
     ```bash
     docker-compose down
     docker-compose up
     ```

### System Requirements for Docker

- Docker Desktop installed
- At least 4GB RAM
- 10GB free disk space
- Internet connection for pulling images

### Security Notes

- Keep your Docker installation updated
- Don't share your environment files
- Use strong passwords for all services
- Regularly check for container updates 


## Contact

For any questions or support, please contact:
- Developer: Nithilan Pahirathan
- Email: nithilan32@gmail.com