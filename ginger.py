"""
    create by Gray 2019-07-08
"""
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError


app = create_app()


# errorhandler可捕捉所有异常，转换成自定义异常类抛出，以防未知的异常不能抛出json给客户端
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 这里最好记录log日志，以方便查看错误原因（本项目未做log）
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
