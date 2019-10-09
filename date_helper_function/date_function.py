from datetime import datetime
from datetime import timedelta

def add_day_to_date_string(date, days=1):
    return((datetime.strptime(date, '%Y-%m-%d') + timedelta(days = 1)).strftime('%Y-%m-%d'))
