# Fitness Tracker API 🏃‍♂️🚴‍♀️🏋️‍♂️

A comprehensive Backend API built with **Django** and **Django REST Framework** to help users log, track, and analyze their daily fitness activities. This project serves as a Capstone Project for the Back-End Web Development program.

## 🚀 Project Overview
The Fitness Tracker API allows users to manage their fitness journey digitally. Users can create accounts, log various types of exercises (Running, Cycling, Weightlifting, etc.), track calories burned, and view their progress over time through a dedicated metrics endpoint.

## ✨ Key Features
- **User Authentication:** Secure signup and login using Django's built-in auth system (extensible to JWT).
- **Activity Management (CRUD):** Full Create, Read, Update, and Delete capabilities for fitness logs.
- **Data Privacy:** Users can only view, edit, or delete their own data.
- **Filtering & Sorting:** Filter activities by type or date range and sort by duration or calories.
- **Activity Metrics:** Summarized data showing total distance, duration, and calories burned over specific periods.
- **Pagination:** Clean, paginated responses for users with long activity histories.

## 🛠 Tech Stack
- **Framework:** Django 5.x
- **API Toolkit:** Django REST Framework (DRF)
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Language:** Python 3.x

## 📂 Project Structure
```text
├── activities/       # Activity logging logic, models, and views
├── users/            # Custom user model and authentication logic
├── core/             # Project settings and URL configurations
├── manage.py         # Django project manager
└── requirements.txt  # Project dependencies



⚙️ Installation & SetupClone the repository:Bashgit clone [https://github.com/mamado143/fitness-tracker-api.git](https://github.com/mamado143/fitness-tracker-api.git)
cd fitness-tracker-api
Create a virtual environment:Bashpython -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:Bashpip install django djangorestframework
Apply migrations:Bashpython manage.py makemigrations
python manage.py migrate
Run the server:Bashpython manage.py runserver
Access the API at http://127.0.0.1:8000/🛣 API Endpoints (Planned)MethodEndpointDescriptionPOST/api/users/register/Register a new userGET/api/activities/List all activities for logged-in userPOST/api/activities/Log a new activityGET/api/activities/{id}/Retrieve a specific activityPUT/api/activities/{id}/Update an activityDELETE/api/activities/{id}/Delete an activityGET/api/activities/metrics/Get total stats (calories, distance)📝 LicenseThis project is for educational purposes as part of a BE Capstone.
---

### Pro-Tip:
Once you save this, run these commands to push it to GitHub so your reviewer can see it:
```bash
git add README.md
git commit -m "docs: add project readme"
git push origin main
