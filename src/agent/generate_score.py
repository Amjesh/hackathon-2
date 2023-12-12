import time
import os
from src.agent.extract_key_points import extract_key_points


def calculate_score(job_description, key_points):
    # Implement your scoring logic based on the defined criteria
    # Example: Count the number of relevant key points matching the job description
    return key_points.lower().count(job_description.lower())


def rank_cvs(job_description, cvs):
    standardized_cvs = [summarize_cv(cv) for cv in cvs]

    results = []
    for idx, cv_text in enumerate(standardized_cvs):
        key_points = extract_key_points(cv_text)
        # Implement your comparison criteria here and assign a numerical score
        # Example: Use a separate function to calculate the score based on key points
        score = calculate_score(job_description, key_points)
        results.append((idx + 1, "Candidate Name", "CV Link",
                       "Experience", "Education", "Highlights", "Don't Meet", score))

    # Sort results by score in descending order
    results.sort(key=lambda x: x[-1], reverse=True)
    return results
