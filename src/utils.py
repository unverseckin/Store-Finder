from flask import make_response, jsonify


class Utils:
    @staticmethod
    def take_distance(elem):
        """A static method that takes an element and returns the value at index 1.

        Parameters:
            elem (any): An element or object.

        Returns:
            any: The value at index 1 of the given element.
        """

        return elem[1]

    @staticmethod
    def custom_error(message, status_code):
        """Creates a custom error response with the provided message and status code.

        Parameters:
        - message (str): The error message to be included in the response.
        - status_code (int): The HTTP status code to be set in the response.

        Returns:
        - Response: A Flask response object with JSON data containing the error message
                    and the specified status code.
        """
        return make_response(jsonify(message), status_code)
