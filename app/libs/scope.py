"""
    Create by GL on 2019-08-09
"""


class Scope:
    allow_api = []
    # 访问一个模块下的所有视图函数
    allow_module = []
    # 排除的视图函数
    forbidden = []

    def __add__(self, other):
        # 运算符重载
        self.allow_api = self.allow_api + other.allow_api
        # 利用集合去重
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    # 可访问user模块下所有视图函数
    allow_module = ['v1.user']

    def __init__(self):
        # self + UserScope()
        pass


class UserScope(Scope):
    # 排除以下不能访问的视图函数
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    # endpoint：
    # v1.red_name+view_func
    splits = endpoint.split('+')
    red_name = splits[0]

    # 在禁止访问中，返回False
    if endpoint in scope.forbidden:
        return False
    # 在允许访问的api
    if endpoint in scope.allow_api:
        return True
    # 在允许访问的模块
    if red_name in scope.allow_module:
        return True
    else:
        return False
