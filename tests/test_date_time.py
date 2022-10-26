from datetime import date # Import date class from datetime module
from datetime import datetime # Import datetime class from datetime module

# https://docs.python.org/3/library/datetime.html

def test_get_todays_date():
    today = date.today()

def test_format_date():
    date_only = date.today()
    date_str = date_only.strftime('%Y-%m-%d') # '2021-01-26'
    print('Current date: ', date_str)

    date_and_time = datetime.today()
    date_time_str = date_and_time.strftime('%Y-%m-%d %H:%M:%S') # '2021-01-26 16:50:03'
    print('Current date and time: ', date_time_str)