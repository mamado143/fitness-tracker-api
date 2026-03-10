
# 🏃‍♂️ Fitness Tracker API

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-a30000?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A comprehensive backend API built with Django and the Django REST Framework (DRF) to help users log, track, and analyze their daily fitness activities. This serves as a Capstone Project for the ALX Back-End Web Development program.

## 🚀 Project Overview

The Fitness Tracker API provides a robust, relational data structure for managing a digital fitness journey. It is designed to handle both standard cardio sessions (tracking duration and calories) and complex resistance training (tracking granular sets, reps, and weight lifted) via nested serialization. 


## ✨ Key Features

* **Custom User Authentication:** Secure email-based registration and login bypassing the default Django username requirement.
* **JWT Security:** Stateless authentication using `djangorestframework-simplejwt` for secure mobile/frontend integration.
* **Nested Serialization:** Create a master `Activity` session and multiple associated `WorkoutSets` in a single, efficient JSON payload.
* **Data Privacy & Permissions:** Strict endpoint security ensuring users can only query, update, or delete their own fitness logs.
* **Advanced Querying:** Global pagination, plus dynamic filtering (by activity type or date) and sorting (by duration or calories) using `django-filter`.
* **Database Aggregation:** A custom `/metrics/` endpoint utilizing Django's ORM (`Sum`, `Count`) to calculate total user statistics on the fly.

## 🛠 Tech Stack

* **Framework:** Django 4.x
* **API Toolkit:** Django REST Framework (DRF)
* **Authentication:** Simple JWT
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Language:** Python 3.x

## ⚙️ Local Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/mamado143/fitness-tracker-api.git](https://github.com/mamado143/fitness-tracker-api.git)
cd fitness-tracker-api
````

**2. Create and activate a virtual environment**

Bash

```
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**

Bash

```
pip install -r requirements.txt
```

**4. Apply database migrations**

Bash

```
python manage.py makemigrations
python manage.py migrate
```

**5. Run the development server**

Bash

```
python manage.py runserver
```

## 🛣 API Endpoints Reference

### Authentication & Users

|**Method**|**Endpoint**|**Description**|**Access**|
|---|---|---|---|
|POST|`/api/users/register/`|Register a new user account|Public|
|POST|`/api/token/`|Obtain JWT access and refresh tokens|Public|
|POST|`/api/token/refresh/`|Refresh an expired access token|Public|

### Fitness Activities

_Note: All activity endpoints require a valid JWT Access Token in the `Authorization: Bearer <token>` header._

|**Method**|**Endpoint**|**Description**|
|---|---|---|
|GET|`/api/activities/`|List all activities (Paginated, supports filtering/sorting)|
|POST|`/api/activities/`|Log a new activity (accepts nested `workout_sets`)|
|GET|`/api/activities/{id}/`|Retrieve a specific activity by ID|
|PUT/PATCH|`/api/activities/{id}/`|Update an existing activity|
|DELETE|`/api/activities/{id}/`|Delete an activity|
|GET|`/api/activities/metrics/`|Get aggregated stats (total workouts, duration, calories)|

## 💡 Example Usage: Logging a Workout

**POST** `/api/activities/`

JSON

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

## 📝 License

This project was developed by Mohamed Dahir Mohamoud for educational purposes as part of the ALX Software Engineering program.



