from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class JobRequest(BaseModel):
    description: str
    required_skills: list
    required_education: str
    location: str
    experience: int
    salary_range: tuple

class CandidateRequest(BaseModel):
    name: str
    skills: list
    education: str
    experience: int
    desired_salary: int
    location: str
    willing_to_relocate: bool

@app.post("/calculate_score")
def calculate_score(job: JobRequest, candidate: CandidateRequest):
    # Call your scoring function here
    score = calculate_match_score(job, candidate)
    return {"score": score}

def calculate_match_score(job, candidate):
    # Dummy scoring logic (replace with your actual logic)
    score = 85  # Placeholder score
    return score
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class JobRequest(BaseModel):
    description: str
    required_skills: list
    required_education: str
    location: str
    experience: int
    salary_range: tuple

class CandidateRequest(BaseModel):
    name: str
    skills: list
    education: str
    experience: int
    desired_salary: int
    location: str
    willing_to_relocate: bool

@app.post("/calculate_score")
def calculate_score(job: JobRequest, candidate: CandidateRequest):
    # Call your scoring function here
    score = calculate_match_score(job, candidate)
    return {"score": score}

def calculate_match_score(job, candidate):
    # Dummy scoring logic (replace with your actual logic)
    score = 85  # Placeholder score
    return score