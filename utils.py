from flask import make_response, jsonify


class Utils:
    @staticmethod
    def take_distance(elem):
        return elem[1]

    @staticmethod
    def custom_error(message, status_code):
        return make_response(jsonify(message), status_code)
