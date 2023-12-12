from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.utils.webhook import call_webhook_with_error
from src.agent.extract_key_points import extract_key_points

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
        job_description = inputs[0].get("job_description")
        result = []

        resp = {
            "name": "selected_candidates",
            "type": "longText",
            "data": "key_points"
        }
        return resp

    except Exception as e:
        print(e)
        logger.error('Getting Error in base_agent:', e)
        raise call_webhook_with_error(str(e), 500)
