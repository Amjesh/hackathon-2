from src.utils.temp_db import temp_data
from src.utils.error_handling import error_handler
from src.config.logger import Logger

logger = Logger()


class AbortController:
    """
    The `AbortController` class provides methods to control the execution flow and stop the execution.

    Methods:
      execution_abort: Stops the execution and returns a success message.

    """

    @classmethod
    def execution_abort(cls):
        """
        Stops the execution and returns a success message.

        Returns:
          dict: A dictionary containing the result and status of the execution stop.

        Raises:
          Exception: If an error occurs during the execution stop.

        """
        try:
            logger.info("AbortController.execution_abort() method called")
            temp_data['isExecutionContinue'] = False
            return {"result": "Execution stopped successfully", "status": "success"}
        except Exception as e:
            logger.error(
                'Getting Error in AbortController.execution_abort:', e)
            raise error_handler(e, 500)
