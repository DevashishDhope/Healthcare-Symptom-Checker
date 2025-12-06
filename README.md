# Healthcare Symptom Checker

A safety-first, AI-powered symptom checker built with FastAPI and Vanilla JS. This tool accepts user symptoms and provides potential conditions and general next steps, strictly adhering to educational purposes only.

## Features

- **Real AI Power**: Integrated with **Google Gemini 2.5** for high-accuracy, context-aware symptom analysis.
- **Safety First**: Includes mandatory educational disclaimers and avoids medical diagnosis.
- **Privacy-Centric**: Stateless architecture ensures no personal health data is stored or logged.
- **Clean Architecture**: Modular backend structure using FastAPI.
- **Simple Frontend**: User-friendly interface for easy interaction.

## Project Structure

```
healthcare_symptom_checker/
├── backend/
│   ├── main.py              # Application entry point
│   ├── models.py            # Pydantic data models
│   ├── routes/
│   │   └── symptom_routes.py # API endpoints
│   ├── services/
│   │   └── llm_service.py    # LLM interaction logic (Gemini 2.5)
│   └── utils/
│       └── safety.py         # Safety checks and constants
├── frontend/
│   ├── index.html           # Main user interface
│   ├── styles.css           # Styling
│   └── script.js            # Frontend logic
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation & Running

### Prerequisites
- Python 3.8+
- pip

### 1. Backend Setup

1.  Navigate to the project directory:
    ```bash
    cd healthcare_symptom_checker
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up Environment Variables:
    Create a `.env` file in the root directory.
    ```env
    LLM_API_KEY=your_google_gemini_api_key_here
    ```
    *Note: The system gracefully falls back to a mock service if no key is present.*

4.  Run the server:
    ```bash
    uvicorn backend.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

### 2. Frontend Setup

1.  Open `frontend/index.html` in your web browser.
2.  Enter symptoms and click "Analyze Symptoms".

## API Usage

**Endpoint**: `POST /api/analyze`

**Request Body**:
```json
{
  "symptoms": "I have a headache and a mild fever."
}
```

**Response**:
```json
{
  "conditions": [
    "Common Cold",
    "Tension Headache"
  ],
  "next_steps": [
    "Rest and hydration",
    "Monitor temperature"
  ],
  "disclaimer": "This is for educational purposes only. Consult a doctor for medical advice. This system does not provide medical diagnoses or treatment instructions."
}
```

## Safety & Disclaimers

This project is designed with strict safety guardrails:
- **No Diagnosis**: The system explicitly states it does not provide diagnoses.
- **Educational Only**: All outputs are framed as educational information.
- **Mandatory Disclaimer**: Every response includes a hardcoded disclaimer.
- **Input Validation**: Basic checks to ensure meaningful input.

## Architecture Decisions

- **FastAPI**: Chosen for speed, automatic documentation, and type safety.
- **Google Gemini 2.5**: Selected for its superior reasoning capabilities and speed (Flash model).
- **Stateless Design**: Intentionally omitted a database to prioritize user privacy and HIPAA-style compliance (Data Minimization).
- **Service Layer Pattern**: Logic is separated from routes (`llm_service.py`) for testability.
- **Mock Fallback**: Ensures the application runs immediately without configuration.
