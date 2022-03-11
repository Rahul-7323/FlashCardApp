from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

class APIError(HTTPException):
    def __init__(self,status_code, error_code, error_message):
        message = {"error_code":error_code, "error_message":error_message, "status":status_code}
        self.response = make_response(jsonify(message), status_code)