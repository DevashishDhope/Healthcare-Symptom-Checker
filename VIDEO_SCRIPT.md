# Video Demonstration Script

**Tone**: Professional yet enthusiastic.
**Goal**: Technical walkthrough showcasing the specific architecture and AI integration.

---

## 1. Introduction
**"Hi everyone, I'm [Your Name], and this is my submission for the Healthcare Symptom Checker project."**

"The challenge was to build a full-stack application that analyzes medical symptoms using an LLM. My solution focuses on three things: **Real-time AI analysis**, **Privacy-First Architecture**, and **Robust Error Handling**."

---

## 2. The Demo (Unique Use Case)
*(Action: Open the `index.html` page in your browser)*

"Let's jump straight into a live demo. I want to test it with something specific to show it's not just using simple keywords."

*(Action: Type the following)*
**Input**: *"I have a sudden sharp pain behind my right eye and my vision is blurry."*

"I click **Analyze Symptoms**... and look at the speed."

*(Action: Point to the results)*

"Because we are using the **Google Gemini 2.5 Flash** model, the response is instant.
It correctly identifies reliable possibilities like **'Cluster Headache'** or **'Acute Glaucoma'**.
It creates a tailored list of next steps, like seeking immediate care, rather than generic advice."

---

## 3. Technical Deep Dive (The Backend Architecture)
"Now, let's look at the code to see how it actually works. I designed the backend using **FastAPI** with a **Clean Architecture** pattern."

*(Action: Show VS Code `backend/` folder)*

"Here is the data flow when I clicked that button:

1.  **Request Handling**: The request hits `symptom_routes.py`. It uses a **Pydantic model** to strictly validate the input type, ensuring no bad data gets through.
2.  **Service Layer**: The controller passes the data to `llm_service.py`. This is where the magic happens.
3.  **AI Integration**: I construct a secure 'System Prompt' that enforces safety rules (like 'Do not diagnose'). Then, it calls the **Google Gemini API** using a REST transport layer I configured for maximum compatibility.
4.  **Response Parsing**: The AI's JSON output is parsed back into a Python object and sent to the frontend.

This separation of concerns makes the code testable and scalable."

---

## 4. Design Decision: Privacy-First (No Database)
"You'll notice I deliberately omitted a database for query history.

"In healthcare, **Data Privacy** is paramount. By designing a **Stateless Architecture**, I ensure that no sensitive personal health information is ever stored on my servers. The data exists only for the duration of the request, minimizing compliance risk."

---

## 5. Conclusion
"In summary: You have a **Stateless, Safe, and Smart** symptom checker powered by the latest **Gemini 2.5 AI** models.

"Thanks for watching!"
