import random
import string
from datetime import datetime

TIMESTAMP_WITH_TIMEZONE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'


class GeneralObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_utc_now():
    return datetime.utcnow()


def set_msg(state, gradeState):
    if state == gradeState:
        msg = 'Assignment is already graded!'
    else:
        msg = 'Only assignment in submitted state can be graded!'
    return msg
