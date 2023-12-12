import openai
import os


def generate_score(job_description, cv_info):
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    cv_text = f"{job_description}\n\nExperience: {cv_info['experience']}\nProjects: {cv_info['projects']}\nSkills: {cv_info['skills']}"

   # Summarize web text using openAI chat completion
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[{
            "role": "user",
            "content": cv_text
        }])

    print(
        f"Summarized with simple method: {response['choices'][0]['message']['content']}")
    return response['choices'][0]['message']['content']
