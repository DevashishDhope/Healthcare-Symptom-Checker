# Demo Video Script

**Duration**: ~2-3 minutes

## 1. Introduction (0:00 - 0:30)
- **Visual**: Show the GitHub Repository or the VS Code project structure.
- **Audio**: "Hi, I'm [Your Name], and this is my submission for the Healthcare Symptom Checker assignment. This project is a full-stack application designed to analyze user symptoms and provide educational guidance using **Google's Gemini 1.5 Flash model** for high-speed, accurate reasoning."

## 2. Architecture Overview (0:30 - 1:00)
- **Visual**: Briefly show the folder structure in VS Code. Open `backend/main.py` and `backend/services/llm_service.py`.
- **Audio**: "The backend is built with FastAPI for high performance and clean architecture. I've structured it with clear separation of concerns:
    - `routes` handle the API endpoints.
    - `services` manage the business logic, specifically the integration with the **Google Gemini API**.
    - `models` define strict data schemas using Pydantic.
    - `utils` enforce safety guardrails."

## 3. Safety Features (1:00 - 1:30)
- **Visual**: Highlight `backend/utils/safety.py` and the system prompt in `llm_service.py`.
- **Audio**: "Safety is the core priority. The system prompt explicitly forbids diagnosis and treatment advice. Additionally, a mandatory disclaimer is hardcoded into the response object in the service layer, ensuring it can never be bypassed by the AI's output."

## 4. Live Demo (1:30 - 2:30)
- **Visual**: Split screen with the running terminal (`uvicorn`) and the frontend (`index.html`) in the browser.
- **Action**: Enter "severe headache and sensitivity to light". Click Analyze.
- **Audio**: "Let's run a live test. I'll enter some symptoms. The frontend communicates with the FastAPI backend, which queries Google Gemini. As you can see, we get a structured response with possible conditions and general next steps. Most importantly, the disclaimer is clearly visible, emphasizing that this is for educational purposes only."

## 5. Conclusion (2:30 - End)
- **Visual**: Show the README.md.
- **Audio**: "The project is fully documented in the README, including installation instructions and API usage. It uses the `google-generativeai` library for robust AI integration. Thank you for watching."
