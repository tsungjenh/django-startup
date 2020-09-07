import logging
from service.biz.user import dao
from service.libs.exception import (
    CustomException,
    ERROR_USER_SYSTEM_ERROR,
    ERROR_USER_NAME_DUPLICATE,
    ERROR_USER_PASSWORD_INCORRECT
)

_LOGGER = logging.getLogger(__name__)


def create_user(name, password):
    user = dao.get_user_by_name(name)
    if user:
        raise CustomException(ERROR_USER_SYSTEM_ERROR)
    user = dao.create_user(name, password)
    return user


def login(name, password):
    user = dao.get_user_by_name(name)
    if not user:
        raise CustomException(ERROR_USER_SYSTEM_ERROR)
    if dao.encode_password(password) != user['password']:
        raise CustomException(ERROR_USER_PASSWORD_INCORRECT)
    return user


def register(name, password):
    user = dao.get_user_by_name(name)
    if user:
        raise CustomException(ERROR_USER_NAME_DUPLICATE)
    user = dao.create_user(name, password)
    return user
