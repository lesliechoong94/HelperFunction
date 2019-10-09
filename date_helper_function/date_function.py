from datetime import datetime
from datetime import timedelta


common_date_format = '%Y-%m-%d'

def dateformat_to_datetime(date_time_string, format=common_date_format):
    """
        StringFormat -> DateTime
    """
    return(datetime.strptime(date_time_string, common_date_format))

def datetime_to_dateformat(datetime, format=common_date_format):
    """
        DateTime -> StringFormat
    """
    return(datetime.strftime(common_date_format))

def add_day_to_date_string(date, days=1):
    """
        DateString -> DateString
    """
    add_date = dateformat_to_datetime(date) + timedelta(days = days)
    return(datetime_to_dateformat(add_date))

def get_timedelta(start_date, end_date):
    """
        get timedelta in int
        2019-10-10 -> 2019-10-01 = 9 days
    """
    return((dateformat_to_datetime(end_date) - dateformat_to_datetime(start_date)).days)


def generate_date_string_range_interval(date, days=0):
    """
        return list of date string
        date could be start date or end date
    """
    return([add_day_to_date_string(date, day) for day in range(0, days)])

def generate_date_string_range(start_date, end_date):
    """
        list of date string
        return [start_date, ... , end_date]
    """
    delta = get_timedelta(start_date, end_date)
    return([add_day_to_date_string(start_date, day) for day in range(0, delta + 1)])
