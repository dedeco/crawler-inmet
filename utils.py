

import time
import datetime


def datestring_to_date(datestr, formatstr="%d/%m/%Y"):
    try:
        dt = time.strptime(datestr, formatstr)
    except ValueError:
        dt = None

    if dt:
        dd = datetime.date(*dt[:3])
    else:
        dd = None

    return dd