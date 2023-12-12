import openai
import os
from src.agent.generate_score import generate_score


def filter_best_cvs(job_description, cvs_data):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    results = []

    for cv_entry in cvs_data:
        file_name = cv_entry["file_name"]
        cv_info = cv_entry["cv_info"]

        # Generate a score for each CV based on the job description
        score = generate_score(job_description, cv_info)

        # Add the CV details and score to the results
        results.append({
            "file_name": file_name,
            "score": score
        })

    # Sort results by score in descending order
    results.sort(key=lambda x: x["score"], reverse=True)

    return results
