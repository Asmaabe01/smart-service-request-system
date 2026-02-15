# Smart Service Request Management System

## 📌 Project Overview

The **Smart Service Request Management System** is a modern web application that allows users to submit service requests and administrators to manage and track those requests securely. The system integrates advanced authentication methods and manages service requests like IT support, maintenance, and other internal services.

This project focuses on backend development using **Python** and **FastAPI** for creating secure, scalable RESTful APIs, with additional functionalities such as **JWT Authentication** and **role-based authorization**.

---

## 🎯 Project Objectives

- Build a secure and scalable backend using **Python** and **FastAPI**.
- Implement modern **authentication** methods including **JWT** and **OAuth2**.
- Create a request management system where users can submit, track, and manage service requests.
- Design a **RESTful API** for communication between frontend and backend.
- Learn backend development through hands-on experience with APIs, databases, and user authentication.

---

## 🛠 Tech Stack

### Backend
- **Python**
- **FastAPI** (for building RESTful APIs)
- **JWT Authentication** (for secure sessions)
- **OAuth2** (for social logins like Google, Facebook)
- **MySQL** (Database for storing user requests and authentication data)
- **SQLAlchemy** (ORM for database interaction)

### Frontend
- **React** or **Vue.js** (for the frontend interface)
- **Tailwind CSS** or **Material UI** (for styling)
- **Axios** (for API calls)

### Tools
- **Git & GitHub** (for version control)
- **Docker** (for containerization)
- **Uvicorn** (for running FastAPI)
- **Swagger** (for API documentation)

---

## 📁 Project Structure

```text
smart-service-request-system/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app entry point
│   │   ├── models.py         # Database models
│   │   ├── routes/           # API endpoints (e.g., auth, requests)
│   │   ├── security/         # Authentication-related files (e.g., JWT)
│   │   ├── services/         # Business logic for managing requests
│   │   └── db.py             # Database connection and setup
├── frontend/                 # React or Vue.js frontend code
└── README.md
