# ShopApp – Software Architecture

## Overview
A simple Flask web application with MySQL database, containerized with Docker.

## Stack
- **Framework:** Flask (Python)
- **Database:** MySQL 8.0 (Docker container)
- **Containerization:** Docker + Docker Compose

## Project Structure
```
shopapp/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Web app container definition
├── docker-compose.yml      # Multi-container setup
├── init.sql                # DB schema + seed data
└── templates/
    ├── base.html           # Shared layout
    ├── login.html          # Login page
    ├── signup.html         # Signup page
    └── search.html         # Product search page
```

## Database Schema

### users
| Column   | Type         | Notes            |
|----------|--------------|------------------|
| id       | INT          | PK, Auto-increment |
| username | VARCHAR(100) | Unique           |
| password | VARCHAR(255) |                  |

### products
| Column      | Type         | Notes            |
|-------------|--------------|------------------|
| id          | INT          | PK, Auto-increment |
| name        | VARCHAR(200) |                  |
| description | TEXT         |                  |

## Application Flow
1. User visits `/` → redirected to `/login`
2. User signs up at `/signup` → credentials saved to `users` table
3. User logs in at `/login` → credentials checked against `users` table → session started
4. Authenticated user accesses `/search` → queries `products` table by name/description
5. Logout at `/logout` → session cleared

## Docker Architecture
```
┌─────────────────────────────────────┐
│          docker-compose             │
│                                     │
│  ┌──────────────┐  ┌─────────────┐ │
│  │  web         │  │  db         │ │
│  │  (Flask)     │→ │  (MySQL)    │ │
│  │  port 5000   │  │  port 3306  │ │
│  └──────────────┘  └─────────────┘ │
│                          │          │
│                    db_data volume   │
└─────────────────────────────────────┘
```

## How to Run Locally
```bash
# Build and start
docker compose up -d

# App available at
http://localhost:5000
```

## How to Deploy to Docker Hub
```bash
# Build image
docker build -t johnpaul/shopapp:latest .

# Login to Docker Hub (Docker Desktop web or CLI)
docker login

# Push image
docker push johnpaul/shopapp:latest
```

## Docker Hub Image URL
https://hub.docker.com/r/johnpaul/shopapp

## Pulling the App (for others)
```bash
docker pull johnpaul/shopapp:latest
docker compose up -d
```
