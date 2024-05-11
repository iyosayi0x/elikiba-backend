
class CustomError(Exception):
    def __init__(self, message, status_code=500):
        """
        Initialize a custom error instance.

        Args:
            message (str): The error message to be associated with this\
                exception.
            status_code (int, optional): The HTTP status code to be used in\
                the response.
                Defaults to 400 (Bad Request).
        """
        super().__init__(message)
        self.status_code = status_code
