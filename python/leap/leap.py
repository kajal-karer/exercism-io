'''
solution to problem leap
'''


def is_leap_year(year: int) -> bool:
    '''
    returns true for leap year
    '''
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
