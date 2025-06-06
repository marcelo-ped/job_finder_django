# Job Finder – Django Job Board App

This is a job board web application built with **Django**. It allows users to search for tech job opportunities, post new job listings, and view details for each job. The app includes full Docker support, with **Nginx as a reverse proxy**, **Gunicorn as WSGI server**, and static file handling via Nginx.

---

## Features

- Search for jobs by title
- Add and view job postings
- Highlight "new" jobs
- Styled with Bootstrap 5 and custom CSS
- Fully containerized with Docker and Nginx
- Static files served by Nginx

---

## Tech Stack

- Django 4.x
- Gunicorn (WSGI server)
- Nginx (reverse proxy & static files)
- Docker + Docker Compose
- SQLite (for development)
- Bootstrap 5

---

## Running the Project with Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/marcelo-ped/job_finder_django.git
cd job_finder_django
```

### 2. Build and start the containers

```bash
docker-compose up --build
```

### 3. Access the app
Open your browser and go to:

```bash
http://localhost/
```