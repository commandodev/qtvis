from datetime import datetime
from jinja2 import Markup
import json
import time

def mk_timestamp(date_str):
    return time.mktime(datetime.strptime(date_str, '%Y-%m-%d').timetuple())

def convert_data(data):
    return [dict(ts=mk_timestamp(row[0]), val=row[2]) for row
            in data[1:]]

def prices(request):
    quote = request.context
    data = dict()
    for k, v in quote.hist.iteritems():
        data[k] = convert_data(v)
    data = Markup(json.dumps(data))
    return dict(msg="hi", historic=data, script_name="prices")
