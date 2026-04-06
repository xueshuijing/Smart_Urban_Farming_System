# Smart Urban Farming – System Architecture


# Smart Urban Farming – System Architecture

## Version 1 Architecture (MVP)

![Version 1 Architecture](system-architecture-v1.png)

---

## Future Architecture (Version 2 & Version 3)

![Future Architecture](system-architecture-future.png)


## Overview

The Smart Urban Farming system is designed using a modular and scalable architecture.  
The goal is to create a clean structure that supports plant data management, user interaction, and future AI and IoT expansion.

The system follows a standard backend architecture where the API communicates with external plant databases and stores structured data in PostgreSQL.

This architecture allows the project to start as a simple MVP and gradually evolve into a smart agriculture research platform.

---

## System Components

The system consists of five main components:

1. Frontend (Future Development)
2. Backend API (FastAPI)
3. PostgreSQL Database
4. External Plant APIs
5. Future AI and IoT Modules

---

## Architecture Diagram

```
User
  |
  v
Frontend (Future Web or Mobile App)
  |
  v
FastAPI Backend
  |
  |----------------------|
  |                      |
  v                      v
PostgreSQL Database    External Plant APIs
                         (Perenual, Trefle)
  |
  v
Future AI & IoT Modules
```

---

## Component Explanation

### 1. Frontend

The frontend will be developed in future versions.

Possible technologies:

- React
- Next.js
- Flutter
- Simple Web Interface

Role:

- User interacts with the system
- Search for plants
- Track plant growth
- View plant care recommendations
- Monitor plant status

In Version 1, the system can run without a full frontend using API testing tools such as Postman or a simple web interface.

---

### 2. Backend (FastAPI)

FastAPI is the core of the system.

Responsibilities:

- Handle API requests
- Communicate with PostgreSQL
- Fetch plant data from external APIs
- Process plant care data
- Store plant information
- Manage user plant collections
- Provide plant recommendations

Example API Endpoints:

```
GET /plants
GET /plants/{id}
POST /plants
GET /plant-care
GET /recommendations
```

This layer connects all system components.

---

### 3. PostgreSQL Database

PostgreSQL stores all structured data.

Main tables:

- plants
- plant_care
- users
- user_plants
- growth_tracking
- recommendations

Responsibilities:

- Store plant data
- Store user data
- Store care schedules
- Store growth records
- Store environmental data in future versions

PostgreSQL ensures reliability and scalability.

---

### 4. External Plant APIs

The system retrieves plant information from external data sources.

### Perenual API

Used for:

- Plant care data
- Watering requirements
- Sunlight requirements
- Basic plant information

### Trefle API

Used in future versions for:

- Global plant database
- Scientific taxonomy
- Advanced plant information

These APIs allow the system to access real-world plant data.

---

### 5. Future AI and IoT Modules

Planned for Version 2 and Version 3.

AI Modules:

- Plant recommendation system
- Growth prediction
- Plant disease detection
- Smart irrigation decision system

IoT Modules:

- Soil moisture sensors
- Temperature sensors
- Humidity sensors
- Smart watering system

This will transform the project into a smart urban farming platform.

---

## Data Flow

### Step 1

User requests plant data.

```
User -> Frontend -> FastAPI
```

---

### Step 2

FastAPI checks database.

```
FastAPI -> PostgreSQL
```

If plant exists, return data.

If not, fetch from external API.

---

### Step 3

Fetch plant data from API.

```
FastAPI -> Perenual API
```

---

### Step 4

Store plant data.

```
FastAPI -> PostgreSQL
```

---

### Step 5

Return result to user.

```
PostgreSQL -> FastAPI -> Frontend -> User
```

---

## System Flow Summary

```
User
  |
  v
Frontend
  |
  v
FastAPI
  |
  |---- PostgreSQL
  |
  |---- Perenual API
  |
  v
Response to User
```

Future expansion:

```
FastAPI -> AI Model
FastAPI -> IoT Sensors
```

---

## Folder Structure

```
smart-urban-farming/

backend/
    app/
        api/
        models/
        services/
        database/
        main.py

database/
    schema.sql

docs/
    system-architecture.md
    technology-selection.md

frontend/ (future)

README.md
```

This structure keeps the project organized and scalable.

---

## Version Architecture

### Version 1

- FastAPI
- PostgreSQL
- Perenual API
- Local deployment

Goal:

Working smart urban farming API.

---

### Version 2

- Trefle API
- AI plant recommendations
- Cloud deployment
- Environmental data

Goal:

Intelligent plant system.

---

### Version 3

- AI models
- IoT sensors
- Smart irrigation
- Predictive analytics

Goal:

Smart urban farming research platform.

---

## Design Principles

### Modular

Each component works independently.

### Scalable

System can grow without restructuring.

### Data-Driven

Uses real plant data and scientific sources.

### Research Ready

Supports AI and smart agriculture development.

---

## Summary

The Smart Urban Farming system architecture consists of:

- FastAPI backend
- PostgreSQL database
- External plant APIs
- Future AI and IoT modules
- Modular and scalable structure

This architecture allows gradual development from MVP to a smart agriculture research
