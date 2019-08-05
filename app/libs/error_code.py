"""
    Create by GL on 2019-08-05
"""
from werkzeug.exceptions import HTTPException


class ClientTypeError(HTTPException):
    code = 400
    description = (
        'client is invalid'
    )
