import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')


def generate_score(job_description, cv_text):
    prompt = f"Job Description: {job_description}\nCV Text: {cv_text}\nScore:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


def process_cvs(job_description, cvs):
    results = []
    for idx, cv_text in enumerate(cvs):
        score = generate_score(job_description, cv_text)
        results.append((idx + 1, "Candidate Name", "CV Link",
                       "Experience", "Education", "Highlights", "Don't Meet", score))
    return results


def display_results(results):
    header = "Rank,Name,CV Link,Experience,Education,Highlights,Don't Meet,Score"
    print(header)
    for result in results:
        print(",".join(map(str, result)))


# Replace with your actual job description
job_description = "Your detailed job description here."

# Replace with your actual CV texts
cvs = [
    """
        I am an experienced Python Developer with a focus on web development using Django and Flask.
        In my previous role at XYZ Corp, I led a team of developers in building scalable and efficient web applications.
        I am proficient in database management using SQL and have worked with both MySQL and PostgreSQL.

        Education:
        - Bachelor of Science in Computer Science, ABC University, Graduated in 2010

        Skills:
        - Python
        - Django
        - Flask
        - SQL
        - MySQL
        - PostgreSQL
        - Web Development

        Experience:
        - Senior Python Developer, XYZ Corp, 2015-2021
        - Led a team of developers in the implementation of web applications.
        - Collaborated with cross-functional teams to define, design, and ship new features.

        Other:
        - Strong problem-solving skills
        - Excellent communication skills
        - Team player

        """,
    "Candidate 2 CV text here.",
    # Add more CVs as needed
]

results = process_cvs(job_description, cvs)
display_results(results)
