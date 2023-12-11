import os
import json
from src.validator.agent import AgentSchema
from src.utils.webhook import call_webhook_with_success, call_webhook_with_error
from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.agent import base_agent

logger = Logger()


class ExecuteController:
    """
    This class represents the controller for executing a task.
    """

    def execute(self, payload: AgentSchema) -> dict:
        """
        Executes the task using the provided payload.

        Args:
          payload (AgentSchema): The payload containing the data for the task.

        Returns:
          dict: The result of the task execution.

        Raises:
          Exception: If an error occurs during task execution.
        """

        try:
            logger.info('ExecuteController.execute() method called')

            # Get payload data
            payload = payload.dict()

            # Here you can write your agent logic.
            # You can use the payload data to perform your task.
            resp = base_agent(payload)

            # Call webhook with success
            call_webhook_with_success({
                "status": 'completed',
                "data": {
                    "info": "Task successfully completed!",
                    "output": resp
                }
            })

            logger.info('Function execute: Execution complete', resp)
            return {"result": resp}
        except Exception as e:
            logger.error('Getting Error in ExecuteController.execute:', e)
            raise call_webhook_with_error(str(e), 500)
