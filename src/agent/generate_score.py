import openai
import os


def generate_score(job_description, cv_info):
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    # Combine relevant information from CV for scoring
    cv_text = f"{job_description}\n\nExperience: {cv_info['experience']}\nProjects: {cv_info['projects']}\nSkills: {cv_info['skills']}"

    # Make a request to OpenAI for scoring
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=cv_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
