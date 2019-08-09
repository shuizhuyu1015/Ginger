"""
    create by Gray 2019-07-11
"""

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    # 以下注释只能抛出ClientTypeError异常，不能抛出其他异常提示，
    # 所以自定义一个form基类BaseForm，自定义校验方法validate_for_api
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()

    # if form.validate():
    #     promise = {
    #         ClientTypeEnum.USER_EMAIL: __register_user_by_email
    #     }
    #     promise[form.type.data]()
    # else:
    #     # wtforms不会抛出异常到视图函数，所以要手动抛出
    #     raise ClientTypeError()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
