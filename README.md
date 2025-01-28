# Physics & Math Academy - Online Courses Platform

![Project Screenshot](./OnlineCourses/static/courses/img/logo.png)

A Django-based web application for managing online courses, user reviews, and contact forms. Designed to help students prepare for exams with structured materials and interactive features.

## Features

- **User Authentication**: Register, login, logout, and access-restricted course materials.
- **Dynamic Content**: 
  - Submit and view approved reviews with ratings.
  - Browse course materials categorized by subject.
- **Contact Form**: Send messages with server-side validation and email notifications.
- **Responsive Design**: Mobile-friendly navigation and layout.
- **Admin Panel**: Manage reviews, users, and course content via Django admin.

## Requirements

- Python 3.8+
- Django 4.2+
- Libraries: See `requirements.txt`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/physics-math-academy.git
   cd physics-math-academy
   ```
2. Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables:
Create a .env file in the project root:

```env
SECRET_KEY=your_django_secret_key
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

5. Run Migrations:

```bash
python manage.py migrate
```

6. Start the Server:

```bash
python manage.py runserver
```

## Usage
- Home Page: Overview of the academy and featured content.
- Courses: Access restricted materials after logging in.
- Reviews: Submit and view student testimonials.
- Contact: Send messages to the admin team.
- Admin Dashboard: Manage data at /admin/ (superusers only).

## Project structure (most important)

```plaintext
OnlineCourses/
├── courses/                          # Main Django app
│   ├── migrations/                   # Database migration files
│   ├── templates/courses/            # App-specific templates
│   │   ├── base.html                 # Base template
│   │   ├── ...                       # Other
│   └── courses/
│       ├── css/
│       │   └── styles.css            # Main stylesheet
│       ├── js/
│       │   └── base.js               # Global JavaScript
│       └── img/                      # All images
├── OnlineCourses/             # Project config
│   ├── __init__.py
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Root URLs
│   └── wsgi.py
├── .env                              # Environment variables
├── manage.py                         # Django CLI
├── requirements.txt                  # Dependencies
└── README.md                         # This file
```

## Pending Tasks
- Password Reset: Implement Django’s PasswordResetView and email templates.
- Data Export: Add XML/XLS export for reviews and courses.
- Edit Reviews: Allow users to update/delete their submissions.
- Enhanced Validation: Add JavaScript for real-time form checks.


