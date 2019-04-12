import sys
import datetime


def GetDate(date_in):
    try:
        datetime.datetime.strptime(date_in, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid Date Format, enter format YYYYY-MM-DD')
    return True


date_input = input("Enter any date: ")
date_today = datetime.datetime.now()
print(str(date_today))
print(str(GetDate(date_input)))
