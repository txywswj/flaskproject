from datetime import datetime


def now():
    return datetime.now().strftime('%Y%d%H%M%S')
