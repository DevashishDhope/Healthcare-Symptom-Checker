# Video Demonstration Script

**Tone**: Excited, clear, and simple (like talking to a friend).
**Goal**: Show off the project and explain why you built it this way.

---

## 1. Introduction (The "Hook")
"Hi everyone! Today I want to show you my project: **The Healthcare Symptom Checker.**

So, the goal of this assignment was to build a smart tool where you can type in your symptoms, and it tells you what might be wrong and what to do next.

The requirements were to use a **Backend API**, connect it to an **AI model**, and make a nice **Frontend** for users. And guess what? I built exactly that!"

---

## 2. The Demo (Show it working!)
*(Action: Open the `index.html` page in your browser)*

"Let me show you how it works. It's super simple.

I’ll type in: *'I have a red rash on my arm and it’s really itchy.'*

I click **Analyze Symptoms**... and boom! Look at that.

*(Action: Point to the results)*

It says it could be **'Contact Dermatitis'** or a **'Fungal Infection'**.
It also gives me smart advice like **'Avoid scratching'** and **'Keep the area clean'**.

And see this down here? **'Your Trusted Health Guide'**. That’s because it’s powered by **Real AI** (Google Gemini), so it’s actually thinking, not just guessing!"

---

## 3. How It Works (The Tech Stuff)
"Okay, so how does this magic happen?

1.  **The Backend**: I used **FastAPI**. It’s like the brain of the operation. It takes what I type and sends it to the AI.
2.  **The AI**: I integrated **Google Gemini 2.5**. This is the cool part—it’s a real intelligence engine that understands medical language.
3.  **The Frontend**: I used simple HTML and JavaScript so it runs fast and looks clean.

I made sure everything focuses on **Safety First**. You’ll see disclaimers everywhere because this is for learning, not for replacing a real doctor."

---

## 4. The "Secret Sauce" (Why no database?)
"You might notice I didn't add a database to save history. That was a **smart choice**.

I wanted this to be a **Privacy-First** tool. When you talk about health, you want your data to be private. So, I designed it to be 'Stateless'—meaning it helps you in the moment and then forgets, so your secrets stay safe. Plus, it makes the app super lightweight!"

---

## 5. Conclusion
"So, that’s my Healthcare Symptom Checker!

 It’s connected to **Real AI**, it’s **fast**, and it respects your **privacy**.

Thanks for watching!"
