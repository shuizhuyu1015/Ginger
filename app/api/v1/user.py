"""
    create by Gray 2019-07-08
"""
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am gray'
