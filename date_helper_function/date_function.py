from datetime import datetime
from datetime import timedelta

def add_day_to_date_string(date, days=1):
    """
        String -> String
    """
    return((datetime.strptime(date, '%Y-%m-%d') + timedelta(days = days)).strftime('%Y-%m-%d'))

def generate_date_string_range(start_date, end_date):
    """
        list of date string 
        return [start_date, ... , end_date]
    """
    return([add_day_to_date_string(start_date, day) for day in range(0,delta.days + 1)])
