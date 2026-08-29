# Personal Task Manager

A full-stack personal task management web application built with **Django**. It allows users to create, manage, organize, and track their tasks through a clean and responsive interface.

Each user has their own private task space, ensuring that tasks created by one user are not accessible to another user.

## Features

### 🔐 User Authentication

* User registration and login
* Secure logout
* Authentication-protected task management
* User-specific task data
* Users can only access their own tasks

### 📋 Task Management

* Create tasks
* View task details
* Edit existing tasks
* Delete tasks
* Mark tasks as completed or pending
* Track task creation and update timestamps

### 🏷️ Task Organization

* Three priority levels:

  * Low
  * Medium
  * High
* Three task statuses:

  * Pending
  * In Progress
  * Completed
* Optional due dates

### 🔎 Search, Filter & Sorting

* Search tasks by title and description
* Filter by task status
* Filter by priority
* Combine search and filters
* Sort by:

  * Newest first
  * Oldest first
  * Due date

### 📊 Dashboard

The dashboard provides an overview of the user's tasks, including:

* Total tasks
* Pending tasks
* In-progress tasks
* Completed tasks
* High-priority tasks
* Today's tasks
* Overdue tasks
* Active tasks
* Recently completed tasks

### 📱 Responsive UI

* Responsive layout for desktop, tablet, and mobile screens
* Consistent navigation across the application
* Task cards and dashboard statistics
* Responsive forms and authentication pages

---

## Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML
* CSS
* Django Templates

### Database

* SQLite during development
* PostgreSQL-ready for production

### Development Tools

* Git
* GitHub
* Python Virtual Environment

---

## Project Structure

```text
personal-task-manager/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── tasks/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── templates/
│   │   ├── registration/
│   │   │   └── login.html
│   │   │
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── dashboard.html
│   │       ├── task_detail.html
│   │       ├── task_form.html
│   │       ├── task_edit.html
│   │       └── task_confirm_delete.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md
```

> `db.sqlite3` is used during local development and should not be committed to the repository in a production setup.

---

## Data Model

The core application revolves around the `Task` model.

Each task contains:

```text
Task
│
├── user
├── title
├── description
├── priority
├── status
├── due_date
├── created_at
└── updated_at
```

The `user` field establishes ownership of each task.

This allows the application to query tasks specifically for the authenticated user:

```python
Task.objects.filter(user=request.user)
```

---

## Authentication & Authorization

The application uses Django's built-in authentication system.

Protected views use:

```python
@login_required
```

Task ownership is also enforced so users can only work with tasks belonging to their account.

The intended access flow is:

```text
New User
   ↓
Sign Up
   ↓
Login
   ↓
Dashboard / Tasks
   ↓
Create & Manage Personal Tasks
   ↓
Logout
```

---

## Search & Filtering

The task list supports multiple query parameters.

Examples:

```text
/tasks/?status=pending
```

```text
/tasks/?priority=high
```

```text
/tasks/?status=pending&priority=high
```

Search can also be combined with filtering and sorting.

For example:

```text
/tasks/?status=pending&priority=high&search=django
```

This allows users to narrow down their task list efficiently.

---

## Dashboard

The dashboard calculates task statistics for the currently authenticated user.

Example metrics:

```text
Total Tasks
Pending
In Progress
Completed
High Priority
```

It also provides task-specific views for:

```text
Today's Tasks
Overdue Tasks
Active Tasks
Recently Completed Tasks
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/personal-task-manager.git
```

Move into the project directory:

```bash
cd personal-task-manager
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Development URLs

| Page         | URL                 |
| ------------ | ------------------- |
| Home / Tasks | `/`                 |
| Task List    | `/tasks/`           |
| Dashboard    | `/tasks/dashboard/` |
| Create Task  | `/tasks/create/`    |
| Login        | `/accounts/login/`  |
| Signup       | `/accounts/signup/` |
| Django Admin | `/admin/`           |

The root URL redirects users to the task list.

Unauthenticated users are redirected to the login page.

---

## Running Tests

Run the Django test suite with:

```bash
python manage.py test
```

If additional test tooling is used, run the corresponding test command documented in the project.

---

## Environment Configuration

For production, sensitive configuration should be provided through environment variables rather than committed directly to GitHub.

Typical production configuration includes:

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
```

A `.env` file can be used locally, but it should be excluded from Git using `.gitignore`.

---

## Security Considerations

The application uses Django's built-in security mechanisms, including:

* CSRF protection
* Authentication
* Password hashing
* Login-required views
* User-specific task queries
* Django form validation

Before production deployment, the project should be configured with:

```text
DEBUG=False
```

and appropriate:

```text
ALLOWED_HOSTS
```

as well as a production database and secure secret configuration.

---

## Future Improvements

Potential future enhancements include:

* Task categories/tags
* Pagination
* Task reminders
* Email notifications
* Recurring tasks
* Calendar view
* REST API
* Drag-and-drop task management
* Dark mode
* Deployment with PostgreSQL
* Automated CI/CD
* Advanced analytics

---

## Learning Goals

This project was built to gain practical experience with:

* Django fundamentals
* Django models and ORM
* Authentication and authorization
* CRUD operations
* Django forms
* Templates
* URL routing
* Query parameters
* Filtering and sorting
* Database migrations
* Static files
* Responsive UI
* Git and GitHub
* Preparing a Django application for deployment

---

## Author

**Kaushal Kumar Jha**

This project was developed as a personal learning and portfolio project to gain hands-on experience building and deploying a Django web application.

---

## License

This project is available for educational and portfolio purposes.
