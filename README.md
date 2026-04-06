# Smart Urban Farming

A scalable smart urban farming system designed to provide plant care recommendations, plant data management, and future AI-based plant monitoring and smart agriculture solutions.

This project aims to build a modular backend system using FastAPI and PostgreSQL while integrating real-world plant databases and supporting future AI and IoT expansion.

---

## Project Goals

- Build a smart plant care management system
- Provide plant watering and sunlight recommendations
- Store and manage plant data
- Integrate external plant databases
- Support future AI-based plant recommendations
- Enable smart urban farming research and development

---

## System Overview

The system uses a modular architecture:

- FastAPI backend
- PostgreSQL database
- External plant APIs
- Future AI and IoT integration

The project starts as a working MVP and expands into a smart agriculture platform.

---

## Architecture

### Version 1 (MVP)

![Version 1 Architecture](docs/system-architecture-v1.png)

---

### Future Architecture (Version 2 & Version 3)

![Future Architecture](docs/system-architecture-future.png)

---

## Technology Stack

### Backend
- FastAPI
- Python

### Database
- PostgreSQL

### External APIs
- Perenual API
- Trefle API (future)

### Future Expansion
- AI models
- IoT sensors
- Smart irrigation
- Cloud deployment

---

## Project Structure

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
    system-architecture-v1.png
    system-architecture-future.png
    technology-selection.md

frontend/ (future)

README.md
requirements.txt
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/xueshuijing/Smart_Watering_System.git
cd smart-urban-farming
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup PostgreSQL

Create database:

```bash
createdb smart_farming
```

Or using PostgreSQL:

```sql
CREATE DATABASE smart_farming;
```

---

### 5. Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

### 6. Open API

```
http://127.0.0.1:8000/docs
```

This opens the Swagger API interface.

---

## API Example

Get plants:

```
GET /plants
```

Get plant by ID:

```
GET /plants/{id}
```

Add plant:

```
POST /plants
```

---

## Documentation

Detailed project documentation is available in the docs folder.

- Technology Selection → docs/technology-selection.md
- System Architecture → docs/system-architecture.md

---

## Version Roadmap

### Version 1

- FastAPI backend
- PostgreSQL database
- Perenual API
- Plant care system

Goal:

Working smart urban farming API.

---

### Version 2

- Frontend dashboard
- Trefle integration
- AI plant recommendation
- Cloud deployment

Goal:

Intelligent plant system.

---

### Version 3

- IoT sensors
- Smart irrigation
- Plant disease detection
- Predictive AI

Goal:

Smart urban farming research platform.

---

## Design Principles

- Modular architecture
- Scalable system
- Data-driven decisions
- Research-oriented development
- Real-world usability

---

## Future Improvements

- Web dashboard
- Mobile application
- Plant image recognition
- Environmental monitoring
- Smart irrigation automation
- Cloud hosting
- AI plant health prediction

---

## License

This project is open-source and available for educational and research purposes.

---

## Author

Smart Urban Farming Project  
AI and Smart Agriculture Research Portfolio

