"""
    create by Gray 2019-07-08
"""
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    # 不能直接序列化的对象才会走default方法，字典可直接序列化
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            # 使用dict将对象序列化，需要在对象中实现keys和__getitem__方法
            return dict(o)

        if isinstance(o, date):
            # 不能序列化的对象，单独在JSONEncoder.default里来处理转化
            return o.strftime('%Y-%m-%d')

        # 不能序列化的抛出异常
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
