# package
import logging
from datetime import datetime
from hashlib import md5
# service
from service.biz.user.models import User

_LOGGER = logging.getLogger(__name__)

_SALT = "V7$#g*BN".encode('utf-8')


def encode_password(passwd):
    return md5(passwd.encode('utf-8') + _SALT).hexdigest()


def create_user(name, password):
    user = User(
        name=name,
        password=encode_password(password),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    user.save()
    return user.to_dict()


def get_user_by_name(name, as_obj=False):
    user = User.objects.filter(name=name).first()
    if not as_obj:
        return user.to_dict() if user else None
    return user
