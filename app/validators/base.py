"""
    Create by GL on 2019-08-06
"""
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        # 重写validate方法，方便不同的异常类抛出不同的msg
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
