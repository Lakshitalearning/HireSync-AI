# 📊 HireSync-AI

**HireSync-AI** is a candidate ranking system that matches job seekers with employer requirements using advanced Machine Learning models. It considers job descriptions and accessory requirements like location, salary, education, and work experience to provide an accurate ranking for each job.

## 📌 **Objective**

Rank candidates for multiple employers based on job descriptions and other criteria, such as:

- Job Description
- Work Location
- Salary
- Education
- Work Experience
- Willingness to Relocate

### 🧠 **How It Works**

1. Employers provide job descriptions and accessory requirements.
2. Candidates input their profiles, including skills, education, location, and other relevant details.
3. The system calculates a match score for each candidate for every job.
4. Outputs a ranked list of candidates for each employer, ordered by best match.

---

## 🛠️ **Tech Stack**

### Backend:
- **Python (FastAPI)**: For handling API requests and processing candidate-job matching logic.
- **Scikit-Learn**: For text vectorization and similarity scoring.
- **Natural Language Processing**: For extracting words for each keyfield 

### Frontend:
- **Streamlit**: For an interactive user interface to input and display results.
- **HTML-CSS-JAVASCRIPT**: For landing page 

### Infrastructure:
- **Docker (Optional)**: For containerizing the application.

---

## 📁 **Project Structure**

```
HireSync-AI/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── utils.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── assets/
│   └── templates/
│
└── README.md
```

---

## 🚀 **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/Lakshitalearning/HireSync-AI.git
cd HireSync-AI
```

### **2. Set Up the Backend (FastAPI)**

```bash
cd backend
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be running at `http://localhost:8000`

### **3. Set Up the Frontend (Streamlit)**

Open a new terminal:
```bash
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

---

## 📊 **System Workflow**

### **1. Input**
- Employer: Job description, required skills, education, location, salary, work experience.
- Candidate: Skills, education, current location, desired salary, experience, willingness to relocate.

### **2. Processing**
- Text vectorization (TF-IDF or Sentence Transformers) for job-candidate matching.
- Compute similarity using Cosine Similarity.
- Rank candidates based on the calculated score.

### **3. Output**
A ranked list of candidates for each employer, ordered by the best match.

Example Output:
Job: Senior WordPress Developer
- PERSON6: Score 74.56%
- PERSON5: Score 74.28%
- PERSON1: Score 72.31%
- PERSON9: Score 70.44%
- PERSON11: Score 70.12%
- PERSON8: Score 68.99%
- PERSON14: Score 68.93%
- PERSON12: Score 68.7%
- PERSON15: Score 67.78%
- PERSON13: Score 64.48%
- PERSON2: Score 60.37%
- PERSON4: Score 59.55%
- PERSON10: Score 55.83%
- PERSON16: Score 53.18%
- PERSON3: Score 53.02%
- PERSON7: Score 48.94%


Job: Graphic Designer
- PERSON8: Score 69.94%
- PERSON6: Score 69.83%
- PERSON9: Score 69.5%
```

---

## 📌 **Key Code Snippets**

### 1. FastAPI Endpoint (backend/main.py)

```python
from fastapi import FastAPI, HTTPException
from models import calculate_score

app = FastAPI()

@app.post("/calculate_score")
async def calculate(job: dict, candidate: dict):
    score = calculate_score(job, candidate)
    return {"score": score}
```

### 2. Candidate Ranking Logic (backend/models.py)

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(job, candidate):
    vectorizer = TfidfVectorizer()
    job_desc = job['description']
    candidate_profile = " ".join(candidate.values())

    vectors = vectorizer.fit_transform([job_desc, candidate_profile])
    score = cosine_similarity(vectors[0], vectors[1])[0][0] * 100
    return round(score, 2)
```

### 3. Streamlit Interface (frontend/app.py)

```python
streamlit run app.py
candidate_name = st.text_input("Candidate Name:")
candidate_skills = st.text_input("Candidate Skills (comma separated):")
candidate_education = st.text_input("Candidate Education:")
candidate_experience = st.number_input("Candidate Experience (years):", min_value=0)
candidate_desired_salary = st.number_input("Candidate Desired Salary:", min_value=0)
candidate_location = st.text_input("Candidate Current Location:")
willing_to_relocate = st.checkbox("Willing to Relocate?")

if st.button("Rank Candidates"):
    job = {
        "description": job_description,
        "required_skills": required_skills.split(","),
        "required_education": required_education,
        "location": location,
        "experience": experience,
        "salary_range": tuple(map(int, salary_range.split("-")))
    }

    candidate = {
        "name": candidate_name,
        "skills": candidate_skills.split(","),
        "education": candidate_education,
        "experience": candidate_experience,
        "desired_salary": candidate_desired_salary,
        "location": candidate_location,
        "willing_to_relocate": willing_to_relocate
    }
```

---
## 📦 **Frontend Samples**
![image](https://github.com/user-attachments/assets/80f7e4d9-2131-4051-bf19-93b7531fffa1)
![image](https://github.com/user-attachments/assets/123ee858-d91a-4448-a7e7-a758d62b7c02)



---


## 🧪 **Testing**

Run the backend tests:
```bash
pytest tests/
```

---

## 📄 **Future Improvements**

- Add multi-language support.
- Adding dynamic weighting system
- Implement a machine learning model for advanced ranking.
- Include a dashboard for better  Graph visualization.

---

## 🤝 **Contributing**

1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request.

---

## 📧 **Contact**
For questions, feel free to reach out via [adityabhaskar201@gmail.com](mailto:your_email@example.com).

