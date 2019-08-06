"""
    Create by GL on 2019-08-05
"""
from app.libs.error import APIException


# 要返回json格式异常，所以自定义了APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


# 专门定义一个代表错误的Exception，以提高代码可读性
class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
