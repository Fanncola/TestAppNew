from flask import jsonify


class Errors:
    @staticmethod
    def error_param():
        data = {
            'error': 'One or more parameters are empty or not filled',
            'error_code': 400
        }
        return jsonify(data), 400

    @staticmethod
    def some_error():
        data = {
            'error': 'Something wrong',
            'eror_code': 500,
        }
        return jsonify(data), 500

    @staticmethod
    def unique_email():
        data = {
            'error': 'Email must be unique',
            'error_code': 400
        }
        return jsonify(data), 400
