# 🏃‍♂️ Fitness Tracker API

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)  
![Django REST Framework](https://img.shields.io/badge/DRF-a30000?style=for-the-badge&logo=django&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  

A **RESTful backend API** built with **Django** and **Django REST Framework** for logging, tracking, and analyzing fitness activities.

This project demonstrates modern backend development practices including **JWT authentication, nested serialization, filtering, pagination, and database aggregation**.

It was developed as a **Capstone Project for the ALX Back-End Web Development Program**.

---

# 🚀 Project Overview

The **Fitness Tracker API** allows users to manage and analyze their personal fitness activities.

The API supports:

- Cardio workouts (duration & calories)
    
- Resistance training with **detailed workout sets**
    
- Secure user authentication
    
- Filtering and analytics of workout data
    

The system is designed with a **relational data structure** where:

User  
 └── Activities  
      └── WorkoutSets

This allows logging a **complete workout session with multiple exercises in one API request**.

---

# ✨ Key Features

### 🔐 Custom Authentication

- Email-based user registration
    
- JWT-based authentication using `djangorestframework-simplejwt`
    
- Secure token refresh workflow
    

### 🏋️ Workout Activity Logging

- Track cardio and resistance training
    
- Log workout notes, duration, and calories
    

### 🔗 Nested Serialization

Create an **activity and multiple workout sets in one request**.

Example:

Activity  
 ├── Set 1  
 ├── Set 2  
 └── Set 3

### 🔎 Advanced Querying

- Pagination
    
- Filtering by activity type
    
- Sorting by calories or duration
    

Powered by `django-filter`.

### 📊 Aggregated Metrics

A custom endpoint provides:

- Total workouts
    
- Total calories burned
    
- Total duration
    

Using Django ORM aggregation:

- `Sum`
    
- `Count`
    

### 🔒 Data Privacy & Permissions

Users can only:

- View their own activities
    
- Update their own records
    
- Delete their own workouts
    

---

# 🛠 Tech Stack

|Technology|Purpose|
|---|---|
|Django|Backend Web Framework|
|Django REST Framework|API development|
|Simple JWT|Token authentication|
|PostgreSQL|Production database|
|SQLite|Development database|
|Python 3.x|Programming language|

---

# 📂 Project Structure

fitness-tracker-api/  
│  
├── users/                 # Custom user model & authentication  
├── activities/            # Activities and workout sets  
│  
├── core/                # Project settings  
│  
├── requirements.txt  
├── manage.py  
└── README.md

---

# ⚙️ Local Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/mamado143/fitness-tracker-api.git  
cd fitness-tracker-api

---

### 2️⃣ Create Virtual Environment

python3 -m venv venv

Activate environment:

**Linux / macOS**

source venv/bin/activate

**Windows**

venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Apply Database Migrations

python manage.py makemigrations  
python manage.py migrate

---

### 5️⃣ Run Development Server

python manage.py runserver

API base URL:

http://127.0.0.1:8000/api/

---

# 🔑 Environment Variables (Optional)

For production deployments create a `.env` file.

Example:

SECRET_KEY=your_secret_key  
DEBUG=True  
DATABASE_URL=postgres://user:password@localhost/db

---

# 🛣 API Endpoints

## Authentication

|Method|Endpoint|Description|
|---|---|---|
|POST|`/api/users/register/`|Register new user|
|POST|`/api/token/`|Obtain JWT token|
|POST|`/api/token/refresh/`|Refresh access token|

---

## Activities

⚠️ All endpoints require authentication.

Header:

Authorization: Bearer <access_token>

|Method|Endpoint|Description|
|---|---|---|
|GET|`/api/activities/`|List activities|
|POST|`/api/activities/`|Create activity|
|GET|`/api/activities/{id}/`|Retrieve activity|
|PUT / PATCH|`/api/activities/{id}/`|Update activity|
|DELETE|`/api/activities/{id}/`|Delete activity|

---

## Metrics Endpoint

|Method|Endpoint|Description|
|---|---|---|
|GET|`/api/activities/metrics/`|Get user fitness statistics|

Example response:
```
{  
  "total_workouts": 12,  
  "total_duration": 540,  
  "total_calories": 3200  
}
```

---

# 💡 Example Request: Logging a Workout

**POST**

/api/activities/
```
{  
  "activity_type": "weightlifting",  
  "duration_minutes": 60,  
  "calories_burned": 300,  
  "notes": "Leg day. Felt strong!",  
  "workout_sets": [  
    {  
      "exercise_name": "Barbell Squat",  
      "set_number": 1,  
      "reps": 5,  
      "weight": "100.00"  
    },  
    {  
      "exercise_name": "Barbell Squat",  
      "set_number": 2,  
      "reps": 5,  
      "weight": "105.00"  
    }  
  ]  
}
```
---

# 🧪 Running Tests

If tests are added:

python manage.py test

---

# 🚧 Future Improvements

- API documentation with **Swagger / OpenAPI**
    
- Docker containerization
    
- Redis caching
    
- Rate limiting
    
- CI/CD pipeline
    
- GraphQL endpoint
    

---

# 📜 License

This project was developed by **Mohamed Dahir Mohamoud** as part of the **ALX Software Engineering Program**.

For educational and portfolio purposes.

---

# ⭐ Support

If you find this project helpful:

⭐ **Star the repository**
