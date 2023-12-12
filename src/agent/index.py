from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.utils.webhook import call_webhook_with_error
from src.agent.generate_score import rank_cvs
from src.agent.output_template import output_template

logger = Logger()

# Your array of objects
templateOutput = [
    {'Rank': 1 + 1, 'Name': 'Prachi Madame', 'CV link': 'file1.pdf', 'Experience': 'Example Experience',
        'Education': 'Example Education', 'Highlights': 'Example Highlights', "Don't Meet Criteria": 'Example Criteria', 'Score': 0.85},
    {'Rank': 2 + 1, 'Name': 'test', 'CV link': 'file2.pdf', 'Experience': 'Example Experience', 'Education': 'Example Education',
        'Highlights': 'Example Highlights', "Don't Meet Criteria": 'Example Criteria', 'Score': 0.75},
    {'Rank': 3 + 1, 'Name': 'test2', 'CV link': 'file3.pdf', 'Experience': 'Example Experience', 'Education': 'Example Education',
        'Highlights': 'Example Highlights', "Don't Meet Criteria": 'Example Criteria', 'Score': 0.92},
    {'Rank': 4 + 1, 'Name': 'test3', 'CV link': 'file4.pdf', 'Experience': 'Example Experience', 'Education': 'Example Education',
        'Highlights': 'Example Highlights', "Don't Meet Criteria": 'Example Criteria', 'Score': 0.88},
]


# This is the base_agent function. This function is called when the agent is executed.
# You can also use the temp_data variable to store data that you want to use in other methods.
# You can use the call_webhook_with_success and call_webhook_with_error methods to call the webhook.
# You can use the logger variable to log your data.
# For return the response you can use see config/agent.json file output section.
def base_agent(payload):
    try:
        logger.info("base_agent() called with ", payload)
        inputs = payload.get("inputs")
        job_description = inputs[0].get("job_description")
        outputHtml = output_template(templateOutput)

        resp = {
            "name": "selected_candidates",
            "type": "longText",
            "data": outputHtml
        }
        return resp

    except Exception as e:
        print(e)
        logger.error('Getting Error in base_agent:', e)
        raise call_webhook_with_error(str(e), 500)
