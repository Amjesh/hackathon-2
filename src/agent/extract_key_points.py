import openai
import time
import os

# Function for key points extraction using OpenAI GPT-3


def extract_key_points(cv_text):
    # Replace 'your-api-key' with your actual OpenAI API key
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract key points from the CV text: {cv_text}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
