from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.utils.webhook import call_webhook_with_error

logger = Logger()


# This is the base_agent function. This function is called when the agent is executed.
# You can also use the temp_data variable to store data that you want to use in other methods.
# You can use the call_webhook_with_success and call_webhook_with_error methods to call the webhook.
# You can use the logger variable to log your data.
# For return the response you can use see config/agent.json file output section.
def base_agent(payload):
    try:
        logger.info("base_agent() called with ", payload)
        inputs = payload.get("inputs")
        job_description = inputs.get("job_description")
        result = []

        # Extract key points from the CVs text
        cv_text = """
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

        """

        key_points = extract_key_points(cv_text)

        # Print the extracted key points
        print("Skills:", key_points['Skills'])
        print("Experience:", key_points['Experience'])
        print("Education:", key_points['Education'])
        print("Other:", key_points['Other'])

        resp = {
            "name": "selected_candidates",
            "type": "longText",
            "data": result
        }

        return resp
    except Exception as e:
        logger.error('Getting Error in base_agent:', e)
        raise call_webhook_with_error(str(e), 500)
