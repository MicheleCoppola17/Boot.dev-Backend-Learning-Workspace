"""
Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format and returns a list of the dates sorted in ascending chronological order.

The sorted() function accepts a second optional parameter, key, which should be set to a function that will be called on each iteration. Its returned value is used as the basis for comparing and sorting the original values.
"""
# My first solution
def format_date(date):
    splitted = date.split("-")
    return (splitted[2], splitted[0], splitted[1])

"""
# Boot.dev's solution
def format_date(date):
    month, day, year = date.split("-")
    return year + month + day
"""

def sort_dates(dates):
    return sorted(dates, key=format_date)
