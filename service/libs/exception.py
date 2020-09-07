import enum


class CustomErrorCode:
    def __init__(self, code, message):
        self.code = code
        self.message = message


# DEFINE ERROR
ILLEGAL_PARAMETER = CustomErrorCode(1, 'Invalid Parameters')
ERROR_USER_INVALID_TOKEN = CustomErrorCode(1005, 'Invalid Token')
SERVER_ERROR = CustomErrorCode(5, 'Server Error')
DATA_ERROR = CustomErrorCode(6, "Data Error")
SESSION_INVALID = CustomErrorCode(7, "User not login")

# EXCEPTION FOR USER MODULE
ERROR_USER_NOT_EXISTS = CustomErrorCode(1001, 'User Not Exists')
ERROR_USER_PASSWORD_INCORRECT = CustomErrorCode(1002, 'Wrong Password')
ERROR_USER_NAME_DUPLICATE = CustomErrorCode(1004, 'User Name Duplicated')


class ExceptionType(enum.Enum):
    REGULAR = 'REGULAR'
    EMERGENCY = 'EMERGENCY'


class CustomException(Exception):
    def __init__(self, error_code, message=None, exception_type=ExceptionType.REGULAR):
        assert isinstance(error_code, CustomErrorCode)
        assert isinstance(exception_type, ExceptionType)
        self.error_code = error_code
        _msg = error_code.message
        if message:
            _msg = '{} - {}'.format(error_code.message, message)
        self.detail_message = _msg
        super(CustomException, self).__init__('code: {}, message: {}, exception_type: {}'.format(
            error_code.code, _msg, exception_type.value))
