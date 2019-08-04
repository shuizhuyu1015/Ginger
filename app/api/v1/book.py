"""
    create by Gray 2019-07-08
"""
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'
