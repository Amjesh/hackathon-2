import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')


def extract_key_points(cv_text):
    try:
        prompt = f"Extract the key points from the following CV text:\n\n{cv_text}\n\nKey Points:"

        response = openai.Completion.create(
            engine="text-davinci-003",  # You can experiment with different engines
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
            temperature=0,  # Adjust as needed, higher values make the output more creative
            stop=None  # You can customize the stop criteria
        )

        key_points = response['choices'][0]['text'].strip()
        return key_points

    except Exception as e:
        print(e)
        return None
