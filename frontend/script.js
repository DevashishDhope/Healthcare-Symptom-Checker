const API_URL = "http://127.0.0.1:8000/api/analyze";

document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const symptoms = document.getElementById('symptoms').value;
    const errorMsg = document.getElementById('error-msg');
    const resultsSection = document.getElementById('results');
    const loadingSection = document.getElementById('loading');

    // Reset UI
    errorMsg.classList.add('hidden');
    resultsSection.classList.add('hidden');
    errorMsg.textContent = '';

    if (!symptoms || symptoms.trim().length < 3) {
        errorMsg.textContent = "Please enter a valid description of your symptoms.";
        errorMsg.classList.remove('hidden');
        return;
    }

    loadingSection.classList.remove('hidden');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptoms: symptoms })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'An error occurred while analyzing symptoms.');
        }

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        errorMsg.textContent = error.message;
        errorMsg.classList.remove('hidden');
    } finally {
        loadingSection.classList.add('hidden');
    }
});

function displayResults(data) {
    const conditionsList = document.getElementById('conditions-list');
    const nextStepsList = document.getElementById('next-steps-list');
    const disclaimerText = document.getElementById('disclaimer-text');
    const resultsSection = document.getElementById('results');

    // Clear previous results
    conditionsList.innerHTML = '';
    nextStepsList.innerHTML = '';

    // Populate Conditions
    data.conditions.forEach(condition => {
        const li = document.createElement('li');
        li.textContent = condition;
        conditionsList.appendChild(li);
    });

    // Populate Next Steps
    data.next_steps.forEach(step => {
        const li = document.createElement('li');
        li.textContent = step;
        nextStepsList.appendChild(li);
    });

    // Set Disclaimer
    disclaimerText.textContent = data.disclaimer;

    // Show Results
    resultsSection.classList.remove('hidden');
}
